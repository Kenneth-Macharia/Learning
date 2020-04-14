'''
Coin Flip Streaks
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

Of course, this is only an estimate, but 10,000 is a decent sample size. Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.
'''

from random import randint

def flip_streak():
    streaks = 0

    for _ in range(10001):
        # Generate list of 100 coin flips
        flips = [randint(0,1) for _ in range(101)]

        # Check for any streaks of 6 heads or 6 tails
        zeros = 0
        ones = 0

        # print('## Exp# {}, flips {}\n'.format(exp_num, flips))

        for flip in flips:
            if flip == 0:
                zeros += 1
                ones = 0
            else:
                ones += 1
                zeros = 0

            # print('*** flip {}, zeros {}, ones {}\n'.format(flip, zeros, ones))

            if zeros >= 6 or ones >= 6:
                # print('&&&&&&&&&&\n')
                streaks += 1
                zeros = 0
                ones = 0

        # print('--- Streaks {}\n'.format(streaks))

    print('Chance of streak: {}'.format(streaks/100))

if __name__ == "__main__":
    flip_streak()