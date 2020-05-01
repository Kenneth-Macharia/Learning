'''
ENSURE YOUR CURRENT DIRECTORY IS THE 'RANDOM QUIZZES FOLDER' BEFORE RUNNING THIS SCRIPT

The Problem:
Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else

The program should:
    1. Creates 35 different quizzes
    2. Creates 50 multiple-choice questions for each quiz, in random order
    3. Provides the correct answer and three random wrong answers for each question, in random order
    4. Writes the quizzes to 35 text files
    5. Writes the answer keys to 35 text files
'''

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files, one for each student
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quiz_file = open(f'capitals_quiz{quizNum + 1}.txt', 'w')
    answer_key_file = open(f'capitals_quiz_answers{quizNum + 1}', 'w')

    # TODO: Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((''* 20) + f'State Capitals Quiz (Form {quizNum + 1})\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for question_num in range(50):
        # TODO: Get right and wrong options
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # TODO: Write the question and answer options to the quiz file.
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')

        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        # TODO: Write the answer key to a file.
        answer_key_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")

    quiz_file.close()
    answer_key_file.close()