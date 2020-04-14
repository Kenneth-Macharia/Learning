'''
This program that poses 10 multiplication problems to the user, where the valid input is the problem’s correct answer
'''
import pyinputplus as pyip
import random, time

num_of_questions = 10
correct_ans = 0

for question in range(num_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f'Question {question}: {num1} x {num2} >'

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.

        pyip.inputStr(prompt, allowRegexes=[f'^{num1*num2}$'], blockRegexes=[('.*','Incorrect!')], timeout=8, limit=3)

    except pyip.TimeoutException:
        print('Out of time')

    except pyip.RetryLimitException:
        print('Out of tries')

    # else blocks can follow an if or elif block, they can optionally follow the last except block. The code inside the following else block will run if no exception was raised in the try block
    else:
        # correct answer
        print('Correct!')
        correct_ans += 1

    time.sleep(1)   # Brief pause to let user see the result.
print(f'Score: {correct_ans} / {num_of_questions}')