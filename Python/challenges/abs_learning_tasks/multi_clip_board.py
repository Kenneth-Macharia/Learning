# A multi-clipboard program
import sys
import pyperclip

TEXT = {
    'agree': 'Yes, I agree. That sounds fine to me',
    'busy': 'Sorry, can we do this later this week or nect week?',
    'upsell': 'Would you consider making this a monhtly donation?'
}

'''
argv is a sys list variable that stores commandline arguments. The 1st item in it is the program file name e.g multi_clip_board.py. The other items are arguments passed on the commandline.
'''

if len(sys.argv) < 2: # Check keyphrase arg was inputed, else warn the user & exit
    print('No arguments supplied! \nUsage: python multi_clip_board.py [keyphrase]')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for \'{keyphrase}\' copied to clipbord')

else:
    print(f'There is no text for \'{keyphrase}\'')