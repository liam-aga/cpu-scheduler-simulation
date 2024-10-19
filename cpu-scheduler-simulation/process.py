# process class: add (push)/ remove (pop) from stack
# creates stacks full of processes (function objects)

from linked_stack import Stack
from function import Function


# Call : Whatever is at front of queue calls a function, after that, it gets moved to the back
#

# RETURN : if main is removed, then print that process was ended.
#          if any processes left on call stack, put at the back of the Queue

class Process:
    def __init__(self, name):
        self.stack = Stack()
        self.stack.push(Function("main"))
        self.name = name

    def call(self, fn):  # fn = function name, Call adds to top of stack
        return self.stack.push(fn)

    def end(self):  # removes 1 from stack
        return self.stack.pop()

    def raise_exception(self):
        if self.stack.peek().flag == 'no':
            print(f' {self.stack.peek()}  ends due to unhandled exception.')
            self.stack.pop()

        elif self.stack.peek().flag == 'yes':
            print(f' {self.stack.peek()}  handled the exception .')

        else:
            print("unknown")

    def peek(self):
        return self.stack.peek()  #return top of stack
