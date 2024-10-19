@Author: Liam Aga, (a solo project)
Created: 9/22/2022
A Python simulation of a CPU scheduler using node-based Queue and Stack implementations. Manages processes, function calls, and exception handling through custom classes.

Functions to know:
START <process name>: Creates a new process and adds it to the queue. Example: START firefox. 
CALL <function name> <can handle exceptions?>: The current process calls a function and moves to the back of the queue. Example: CALL play no. 
RETURN: The current process returns from a function. If no functions remain, the process ends. 
RAISE: The current process raises an exception. Functions are popped until one can handle the exception or the process ends.
