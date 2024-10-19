# @author Liam Aga
# Linked Queue class

"""
enqueue: add ot back of the queue
dequeue: remove the front of the queue
peek_front: peek at front value
is_empty: is queue empty

"""

from node import Node


class Linked_Queue:
    def __init__(self):
        self._front = None
        self._back = None

    def is_empty(self):
        # is the Q empty? return bool
        if self._front is None:
            return True
        else:
            return False

    def enqueue(self, entry):
        if self.is_empty():
            node = Node(entry)
            self._back = node
            self._front = self._back
            self._front.next = self._back


        elif self._front.entry == self._back.entry:
            temp = Node(entry)
            self._back.next = temp
            self._front = self._back
            self._back = temp
            self._front.next = temp

        else:
            temp = Node(entry)
            self._back.next = temp
            self._back = temp


        # place the entry in a node
        # add the node to the back

    def dequeue(self):
        # remove the fronts and returns it
        if self.is_empty():
            raise RuntimeError

        elif self._front == self._back:
            temp1 = self._front
            self._front = None
            self._back = None
            return temp1.entry

        else:
            temp1 = self._front
            self._front = temp1.next
            return temp1.entry

    def peek_front(self):
        # check for an empty queue
        if self._front:
            return self._front.entry
        else:
            raise RuntimeError
