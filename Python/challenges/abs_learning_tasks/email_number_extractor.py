'''
PROBLEM: Find every phone number and email address in a long web page or document.
'''
'''
SOLUTION: Write a rogram thar saves the entire document to the clipboard, finds and replaces the clipboard text with the phone numbers and email address found, ready for pasting to destination.
'''
'''
SOLUTION TASKS:
    1. Get the text off the clipboard.
    2. Find all phone numbers and email addresses in the text.
    3. Paste them onto the clipboard.
'''
'''
SOLUTION STEPS:
    1. Use the pyperclip module to copy and paste strings.
    2. Create two regexes, one for matching phone numbers and the other for matching email addresses.
    3. Find all matches, not just the first match, of both regexes.
    4. Neatly format the matched strings into a single string to paste.
    5. Display some kind of message if no matches were found in the text.
'''

import re, pyperclip

# TODO: Create email phone regex
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Non-greedy mode for the first match of aread code; either 444 or (444)
    (\s|-|\.)?  # Match a space or tab followed by a '-' or a '.'
    (\d{3}) # next 3 digits
    (\s|-|\.)   # Match a space or tab followed by a '-' or a '.'
    (\d{4}) # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # optional extension made up of any number of spaces followed by ext, x, or ext., followed by two to five digits.

)''', re.VERBOSE)

# TODO: Create email regex
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username character class: any lower or upper case char, digit, '.', '%', '_', '-', '+'
    @   # @ symbol
    [a-zA-Z0-9.-]+  # domain character class: any of those characters is legal
    (\.[a-zA-Z]{2,4})   # Top-level-domain e.g .com: a '.' followed by any of the chars in the character class, limited to 2 - 4 characters long.

)''', re.VERBOSE)

# TODO: Find matches in clipboard (paste clipboard content, use findall to get matches
text = str(pyperclip.paste())   # fetch clipboard data

matches = []    # stores the matches as tuples

for groups in phone_regex.findall(text):
    # built valid numbers from phone # match groups: [1]:'area code', [3]:'first 3 digits', [5]:'last four digits'
    phoneNum = '_'.join([groups[1], groups[3], groups[5]])

    if groups[8] !='':  # If an extension is found for a number, add 'x' and the extension
        phoneNum += ' x' + groups[8]    # [8]:'the extension number only'

    matches.append(phoneNum)    # add the phone number to matches list

for groups in email_regex.findall(text):
    matches.append(groups[0])   # group[0] is an entire match string

# TODO: Copy results back to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Phone numbers and email addresses found and copied to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addresses found')