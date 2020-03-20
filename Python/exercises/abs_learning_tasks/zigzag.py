'''
A Short Program: Zigzag
Let’s use the programming concepts you’ve learned so far to create a small animation program. This program will create a back-and-forth, zigzag pattern until the user stops it by pressing the Mu editor’s Stop button or by pressing CTRL-C. When you run this program, the output will look something like this:

    ********
   ********
  ********
 ********
********
 ********
  ********
   ********
    ********

'''

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