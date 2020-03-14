# Prints a continous zigzag
from time import sleep

def zigzag():
    indent_spaces = 0
    increase_indentation = True

    while True:
        print(' '*indent_spaces, end='')
        print('*********')
        sleep(0.1)

        if increase_indentation:
            indent_spaces +=1

            if indent_spaces == 20:
                increase_indentation = False

        else:
            indent_spaces -=1

            if indent_spaces == 0:
                increase_indentation = True

zigzag()