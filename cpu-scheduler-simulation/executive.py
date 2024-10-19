# executive.py @author Liam Aga  3050093 9/22/2022 | lab2 TA: S.Awan | This lab demonstrates the use of linked queues
# and stacks in order to implement a mock CPU scheduler by manipulating object-oriented design.
from process import Process
from scheduler import Scheduler
from function import Function


class Executive:
    def __init__(self, file_name):
        self.file_name = file_name
        self.cmds = []

    def txt_clean(self):
        file = open(self.file_name, "r")
        list1 = []

        for line in file:  # this for loop cleans the text files and stores it in a list to then use.
            line_strip = line.strip(" ").strip("\n")
            line_split = line_strip.split()
            list1.append(line_split)
            self.cmds = list1

        file.close()

    def function_create(self):  # applications like iTunes is a process
        new_scheduler = Scheduler()
        for x in self.cmds:
            if x[0] == "START":
                new_process = Process(x[1])  # "main" is automatically instantiated w/ START
                new_scheduler.start(new_process)
                print(f'{str(x[1])} was added to the queue')

            elif x[0] == "CALL":

                current_process = new_scheduler.peek_front()  # this can use process methods
                if x[2] == "no":
                    x[2] = False
                elif x[2] == "yes":
                    x[2] = True
                current_func = Function(x[1], x[2])
                current_process.call(current_func)
                print(f'{current_process.name} called {current_func.name}...')
                var = new_scheduler.dequeue()
                new_scheduler.start(var)  # enqueues the var

            elif x[0] == "RETURN":
                # if return reaches main, end process and print message.
                # call process at the front of the queue to return Function at the top of the stack
                current_process = new_scheduler.peek_front()
                var = current_process.peek()
                if var.name == "main":
                    # if it is main, remove it (pop it) and maybe dequeue
                    current_func = current_process.peek()
                    # print(new_scheduler.queue._front.entry.name)
                    new_scheduler.dequeue()
                    print(f'{current_process.name} returns from {current_func.name} ...')
                    print(f'{current_process.name} process has ended...')
                else:
                    current_func = current_process.peek()
                    # var2 = new_scheduler.queue._front.entry.name
                    print(f"{current_func.name} was returned. ")
                    var = new_scheduler.dequeue()
                    new_scheduler.start(var)
                    # print(var2)  #prints front node of queue

            elif x[0] == "RAISE":  # pop the Functions
                current_process = new_scheduler.peek_front()
                current_func = current_process.peek()

                # loop .pop until main is reached or flag == True
                print(f'{current_process.name} encountered a raised exception by: {current_func.name} ')
                y = True
                while y:
                    try:
                        current_func = current_process.peek()
                    except:
                        y = False
                    if current_func.name == "main":
                        print(f'{current_process.name} process has ended...')
                        new_scheduler.dequeue()
                        y = False

                    else:
                        if current_func.flag == True:
                            print(f'{current_process.name} has exception handled by: {current_func.name}. ')
                            y = False

                        else:
                            print(f'{current_process.name} ends {current_func.name} due to unhandled exception. ')
                            current_process.end()  # this does the pop function

            else:
                print("Error command not found. ")
