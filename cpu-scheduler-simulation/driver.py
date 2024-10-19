# driver.py
# @ author Liam Aga
from executive import Executive


def main():
    file_input1 = input("enter the name of the file: ")
    # file_input1 = "input.txt"
    my_exec = Executive(file_input1)
    my_exec.txt_clean()
    my_exec.function_create()


main()
