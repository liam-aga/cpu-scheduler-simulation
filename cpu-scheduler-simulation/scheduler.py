from linked_queue import Linked_Queue



# CPU uses a queue full of stacks
# this class mimics the methods as of linked Queue


class Scheduler:
    def __init__(self):
        # self.file_name = file
        self.queue = Linked_Queue()

    def start(self, process):
        return self.queue.enqueue(process)
        # enqueue creates the node for process
        # print(f'{Process()} added to the queue ')

    def peek_front(self):  # this will access the front of the queue, and the top of its stack.
        return self.queue.peek_front()

    def dequeue(self):  # removes front of Q
        return self.queue.dequeue()
