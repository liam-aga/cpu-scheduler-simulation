# linked stack
# @author Liam Aga

from node import Node


class Stack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        my_node = Node(entry)
        my_node.next = self._top
        self._top = my_node

    def is_empty(self):
        if self._top is None:
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            top = self._top
            self._top = self._top.next
            return top
        else:
            raise RuntimeError

    def peek(self):
        if self.is_empty():
            raise RuntimeError
        else:
            return self._top.entry
