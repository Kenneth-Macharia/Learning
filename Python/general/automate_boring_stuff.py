print('------------- *** DICTINARIES *** --------------------------')
# Use of get() and setdefault methods
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'pretzels': 4}}
totals = {}

def item_total():
    for persons_basket in allGuests.values():
        for item, count in persons_basket.items():
            if item not in totals:
                totals.setdefault(item, count)
            else:
                totals[item] = totals.get(item, 0) + count

    print(totals)

item_total()

# Counting the char occurrences in a string
string = '#This is a string for the char count test 1'
char_count = {}

for char in string:
    char_count.setdefault(char, 0)
    char_count[char] += 1
char_count

print('\n------------- *** STRINGS *** --------------------------')
# ESCAPE CHARACTERS enable the use of 'invalid' string characters within string literals e.g ", ', \, t, n that should be treated as part of the string.

# invalid_str : 'Bob's mum'
# valid_str : "Bob's mum" or 'Bob\'s mum or 'Bob\n' mum'


# RAW STRINGS: achieved by preceesing a string with 'r' then all escape charaters are ignored and treated as part of the string e.g:

s1 = r'C:\root\folder>'
print(s1) # C:\root\folder>

s2 = r'^(?P<pk>\d+)/'
print(s2) # ^(?P<pk>\d+)/

# Use DOC STRINGS for muli-lines strings instead of line breaks ie. \n even in print statements, all escape charaters are ignored as well:
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# NOT and NOT IN keywords can be used in string just like in lists

# STRING INTERPOLATION is inserting strings into other string e.g
v1 = 'Ken'
v2 = 36

s1 = r'My name is %s and\I am %s years old' %(v1, v2-1)
print(s1)

s2 = f'My name is {v1} and I am {v2-1} years old'
print(s2)

s3 = rf'My name is \{v1} and I am {v2-2} years old'
print(s3)

# STRING METHODS: https://www.programiz.com/python-programming/methods/string are very useful in validating strings e.g passwords

print('ABC'.join(['My', 'name', 'is', 'Simon']))

print('''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''.split('\n'))

print('Hello, world!'.partition(','))
print('Hello, world!'.partition('.'))

print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20, '='))

# Remove whitespaces(' '), tabs(\t) and new line(\n) with strip() methods
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))
print('SpamSpamBaconSpamEggsSpamSpam'.strip('mapS'))
print('SpamSpamBaconSpamEggsSpamSpam'.strip('Spam'))

# Use the ord() and char() methods to convert string character to and from UNICODE
unicoded = ord('!')
print(unicoded)
print(chr(unicoded))

unicoded = ord('4')
print(unicoded)
print(chr(unicoded))

unicoded = ord('A') + 1
print(unicoded)
print(chr(unicoded))

print(ord('C') > ord('c'))

print('\n------------- *** METHODS *** --------------------------')
# https://realpython.com/instance-class-and-static-methods-demystified/


print('\n------------- *** REGEX *** --------------------------')
# You may be familiar with searching for text by pressing CTRL-F and entering the words you’re looking for. Regular expressions go one step further: they allow you to specify a pattern of text to search for e.g:

# American phone numbers: have hyphens in specific locations 415-555-1234
# email addreses: have @
# URLs: have ://
# hashtags: start with #

# To match a phone number of the form: 444-222-1234, the regex '\d\d\d-\d\d\d-\d\d\d\d
# works, Python knows \d stands for a digit, so match such a pattern. It can be simplified as \d{3}-\d{3}-\d{4}

# Regex objects  can be created with match patterns then applied on string to determine if the match pattern exists in the string using the search() which returns the FIRST-match OBJECT, which contains details of the match found.

import re

phone_number_regex_object = re.compile(r'\d{3}-\d{3}-\d{4}')
match = phone_number_regex_object.search('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
print(f'Match found: {match}, {match.group()}')

# Matching sub-strings of the entire string via groups. Using parenthesis in the match pattern will create subgroups in the matched string, accessible via group id specified in the group(). Passing no args to group() returns the entire match.

area_code_match = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
s = 'Call me at 415-555-1011 tomorrow.'
print(f'Matched area code: {area_code_match.search(s).group(1)}')

# (NB) Using groups, returns all the groups matched
print(f'Matched area code: {area_code_match.search(s).groups()}')

# Escaping special regex characters e.g () used in grouping
match_pattern = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')
s = 'Call me at 415-555-1011 tomorrow. (415)-555-9999 is my office.'
match = match_pattern.search(s)
first_part, second_part, last_part = match.groups()
print(f'1st:{first_part}, 2nd:{second_part} 3rd:{last_part}')

# All these are special characters in REGEX : .  ^  $  *  +  ?  {  }  [  ]  \  |  (  ) and must be escaped, if they are to be included in the search pattern as follows:
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)

# Use the PIPE | symbol to match either or string, the first occurence of which, is returned to the search object.

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batma and Tina Fey')
print(f'##### {mo1.group()}')

# Optional matching with '?'. The (wo)? part of the regular expression means that the pattern wo is an optional group. The regex will match text that has zero instances or one instance of wo in it. This is why the regex matches both 'Batwoman' and 'Batman'.
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# Marching Zero or more with '*'. For 'Batman', the (wo)* part of the regex matches zero instances of wo in the string; for 'Batwoman', the (wo)* matches one instance of wo; and for 'Batwowowowoman', (wo)* matches four instances of wo.
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# Matching ATLEAST on or more with '+'. Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once. It is not optional.
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

# Matching repetition using {}. Above we saw you can match repeated digits using \d{3} &
# \(d{3}), this can be extended to specify no-specific repetitions:
# ('Ha'){3,} : matches 3 or more 'Ha'
# ('Ha'){,3} : matches zero to 3 'Ha'
# ('Ha'){3,5} : matches 3 to 5 'Ha'

# Greedy vs Non-greedy matching
# Python regex are greedy by default ie. in ambiguous situations they will match the longest string possible
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())  # Matches the longest 'Ha'*5 though *3 & *4 are also valid matches.

# Non-greedy matches are specified using the '?' (Note this is stil used for optional matching, which are not related)
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())  # Matches the least 'Ha'*3 and not the default 'Ha'*5

# The findall() method returns the STRINGS of all matches found as opposed to search which return the first match only.
phone_number_regex_object = re.compile(r'\d{3}-\d{3}-\d{4}')
search_match = phone_number_regex_object.search('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
findall_match = phone_number_regex_object.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
print(f'Search: {search_match.group()} vs findall: {findall_match}')

# (NB) Findall returns a list of strings, if there are no groups in the regex, else, it returns  list if tuples, each representing a match found.
phone_number_regex_object_grp = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
findall_match = phone_number_regex_object_grp.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
print(f'Findall (groups): {findall_match}')

# There are many Shorthand Character Classes such as \d standing for the regex ((0|1|2|3|4|5|6|7|8|9)) available.

'''
    \d : Any numeric digit from 0 to 9.
    \D : Any character that is not a numeric digit from 0 to 9.
    \w : Any letter, numeric digit, or the underscore character. (Think of this
        as matching “word” characters.)
    \W : Any character that is not a letter, numeric digit, or the underscore character.
    \s : Any space, tab, or newline character. (Think of this as matching
        “space” characters.)
    \S : Any character that is not a space, tab, or newline.
'''

# The character class [0-5] will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5).
xmasRegex = re.compile(r'\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8_maids, 7 \
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# Custom Character Classes when the default ones (\d, \D, \w, \W, \s, \W) are too broad, using square bracket '[]'
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

alpha_numeric_regex = re.compile(r'[a-zA-Z0-9]')
print(alpha_numeric_regex.findall('RoboCop2 eats baby food. BABY FOOD.'))

numeric_regex = re.compile(r'[0-9]')
print(numeric_regex.findall('RoboCop2 eats baby food. BABY FOOD.'))

# (NB) The caret symbol can be used to negate custom regex
non_vowel_regex = re.compile(r'[^aeiouAEIOU]')
print(non_vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

non_numeric_regex = re.compile(r'[^0-9]')
print(non_numeric_regex.findall('RoboCop2 eats baby food. BABY FOOD.'))

# The caret symbol '^' at the beginning of a regex specifies that the match must be found at the beginning of the search string and the dollar sign '$' enforces matches a the end.
# The ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.
beginsWithHello = re.compile(r'^Hello')  # Start with 'Hello
print(beginsWithHello.search('Hello, world!'))
print(beginsWithHello.search('He said Hello.') == None)

endsWithNumber = re.compile(r'\d$')  # End with digit
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None)

wholeStringIsNum = re.compile(r'^\d+$')   # start, end and match digits exactly
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12  34567890') == None)

# Wildcard character '.' which matches every character (single) except '\n'. Use '.*' to match everything.
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex = re.compile(r'.*at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

#For example, say you want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and then followed by anything again. You can use the dot-star (.*) to stand in for that “anything.”
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# The dot-star uses greedy mode: It will always try to match as much text as possible. To match any and all text in a non-greedy fashion, use the dot, star, and question mark (.*?)Like with braces, the question mark tells Python to match in a non-greedy way.
# Both regexes roughly translate to “Match an opening angle bracket, followed by anything, followed by a closing angle bracket.” But the string '<To serve man> for dinner.>' has two possible matches for the closing angle bracket. In the non-greedy version of the regex, Python matches the shortest possible string: '<To serve man>'. In the greedy version, Python matches the longest possible string: '<To serve man> for dinner.>'.
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# Matching everything including '\n', add re.DOATALL as 2ns arg to compile(), when generating the regex.
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group())

print('--------------')

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group())

# Case Insensitive regex. Because regexs are specific, they are case sensitive. To make them case insensitive, add re.IGNORECASE or re.I as a second argument to re.compile()

# String substitution can be done where matches are found (find & replace) using the sub()
# The first argument is a string to replace any matches. The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# (NB) You can also use matched strings as inputs to the sub(), e.g \1, \2, \3 can be passed as the 1st arg to sub() to use the 1st, 2nd or 3rd matched groups in the substitutions.

# to censor the names of the secret agents by showing just the first letters of their names. To do this, you could use the regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1 in that string will be replaced by whatever text was matched by group 1—that is, the (\w) group of the regular expression.
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.'))

# Complex Regex: Regular expressions are fine if the text pattern you need to match is simple. But matching complicated text patterns might require long, convoluted regular expressions. You can mitigate this by telling the re.compile() function to ignore whitespace and comments inside the regular expression string. This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().

# Complex regex:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4} \
(\s*(ext|x|ext.)\s*\d{2,5})?)')

# More readeable version of the above:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Combining many arguments passed to re.compile using the pipe character '|' since re.compile only takes one second argument
# What if you want to use re.VERBOSE to write comments in your regular expression but also want to use re.IGNORECASE to ignore capitalization? Unfortunately, the re.compile() function takes only a single value as its second argument. You can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|), which in this context is known as the bitwise or operator.
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

print('\n------------- *** INPUT VALIDATION *** --------------------------')
# Input validation code checks that values entered by the user, such as text from the input() function, are formatted correctly. For example, if you want users to enter their ages, your code shouldn’t accept nonsensical answers such as negative numbers (which are outside the range of acceptable integers) or words (which are the wrong data type). Input validation can also prevent bugs or security vulnerabilities.

# However, writing input validation code for every  call in your program quickly becomes tedious. Also, you may miss certain cases and allow invalid input to pass through your checks.

# ROBUST input validation via the PyInputPlus Module: PyInputPlus contains functions similar to input() for several kinds of data: numbers, dates, email addresses, and more.

# https://pypi.org/project/PyInputPlus/
# https://pyinputplus.readthedocs.io/en/latest/

# If the user ever enters invalid input, such as a badly formatted date or a number that is outside of an intended range, PyInputPlus will reprompt them for input just like our code in the previous section did. PyInputPlus also has other useful features like a limit for the number of times it reprompts users and a timeout if users are required to respond within a time limit.

# Pip install pyinputplus to use it.

import pyinputplus as pyip

# response = pyip.inputInt(prompt='Enter an integer: ')
# print(response)


# The inputNum(), inputInt(), and inputFloat() functions, which accept int and float numbers, also OPTIONAL have min, max, greaterThan, and lessThan keyword arguments for specifying a range of valid values

# response = pyip.inputNum('> ', min=4, lessThan=6)
# print(response)


# By default, blank input isn’t allowed unless the blank keyword argument is set to True.

# response = pyip.inputNum('Enter num: ', blank=True)
# print(response)

# limit kwarg: raises exceptin after a certain number of tries
# timeout kwarg: raise exception if input entered after a certain amount of time
# default kwarg: when used alongise the above two, its value is taken as input, instead of an exeption being thrown.

# print(pyip.inputNum(limit=2))

# print(pyip.inputNum(timeout=5))

# print(pyip.inputNum(limit=2, default='N/A'))


# The allowRegexes and blockRegexes Keyword Arguments. You can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.

# For example, enter the following code into the interactive shell so that inputNum() will accept Roman numerals in addition to the usual number:

# print(pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+'])) (1 more of either these chars)

# Enter the following into the interactive shell so that inputNum() won’t accept even numbers:

# print(pyip.inputNum(blockRegexes=[r'[02468]$']))  (numbers ending in either of these)

# If you specify both an allowRegexes and blockRegexes argument, the allow list overrides the block list. For example, enter the following into the interactive shell, which allows 'caterpillar' and 'category' but blocks anything else that has the word 'cat' in it:

# print(pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
# blockRegexes=[r'cat']))

# Custom validation fucntion passed to inputCustom().

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers)

# print(pyip.inputCustom(addsUpToTen))

# NB: We are passing the addsUpToTen() function itself to inputCustom(), not calling addsUpToTen() and passing its return value, hence no parenthesis.
# The inputCustom() function also supports the general PyInputPlus features, such as the blank, limit, timeout, default, allowRegexes, and blockRegexes keyword arguments

print('\n------------- *** READING AND WRITING FILES *** --------------------------')
# The C:\ part of the path is the root folder, which contains all other folders. On Windows, the root folder is named C:\ and is also called the C: drive. On macOS and Linux, the root folder is /. In this book, I’ll use the Windows-style root folder, C:\. If you are entering the interactive shell examples on macOS or Linux, enter / instead.

# Additional volumes, such as a DVD drive or USB flash drive, will appear differently on different operating systems. On Windows, they appear as new, lettered root drives, such as D:\ or E:\. On macOS, they appear as new folders under the /Volumes folder. On Linux, they appear as new folders under the /mnt (“mount”) folder. Also note that while folder names and filenames are not case-sensitive on Windows and macOS, they are case-sensitive on Linux.

# Back slashes are used to separate path folders on Windows and forward slashes on Unix-like systems. For pythin script to interact properly with either systems, the correct separator needs to be used.
# The Path() function in the pathlib module will return the correct path (with the correct separator for the system it is run on) when su-plied with the folder names.

from pathlib import Path
print(Path('root', 'Users', 'kenneth', 'Documents'))

# Path() returns a WindowsPath or PosixPath object (depending on the OS), that can be passed to other file-related fucnctions for further manupulation.

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(rf'C:\Users\Al{filename}'))

# (NB) '\' can't be used a part of folder or file names on Windows, but can on Unix-like systems and vice versa for '/'. Use '/' in Python in conjuction with Path(), which will sort all this out on every OS.
# The / operator that we normally use for division can also combine Path objects and strings. This is helpful for modifying a Path object after you’ve already created it with the Path() function, which is safer than using join() or any other str concatenation method, BUT atleast one of the values must be a Path() object.

print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon', 'eggs'))

# print('spam' / 'bacon' / 'eggs')    Raises TypeError

# Python evaluates the / operator from left to right and evaluates to a Path object, so either the first or second leftmost value must be a Path object for the entire expression to evaluate to a Path object. To fix the above, we need to add a Path() obj to the left of the above e.g

print(Path()/ 'spam' / 'bacon' / 'eggs')
print(Path('root')/ 'spam' / 'bacon' / 'eggs')

# (NB) The non-robust way is to use str concatenation but check the OS (sys.platform) to decide which separator to use.

# Every program that runs on your computer has a current working directory, or cwd. Any filenames or paths that do not begin with the root folder are assumed to be under the current working directory.

# You can get the current working directory as a string value with the Path.cwd() function and change it using os.chdir()

import os

print(Path.cwd())

os.chdir('/Users/kenneth/Documents/Code-practise/Python/')
os.chdir('../../')

print(Path.cwd())

# The old way of getting the cwd
print(os.getcwd())

# All users have a folder for their own files on the computer called the home directory or home folder. You can get a Path object of the home folder by calling Path.home()

print(Path.home())

r''' The home directories are located in a set place depending on your operating system:

        On Windows, home directories are under C:\Users.
        On Mac, home directories are under /Users.
        On Linux, home directories are often under /home.

    Your scripts will almost certainly have permissions to read and write the files under your home directory, so it’s an ideal place to put the files that your Python programs will work with.
'''

# An absolute path, which always begins with the root folder while a relative path, which is relative to the program’s current working directory.
# There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.” ie.
# ./ > current directory & ../ > parent directory of the current directoy. The ./ is however optional.

# Create new directories using the os.makedirs()
print('-------')
os.chdir('/Users/kenneth/Documents/Code-practise/Python/general')
print(Path.cwd())
os.makedirs(Path.cwd()/ 'test')
os.chdir(Path.cwd()/ 'test')
print(os.getcwd())
os.chdir('/Users/kenneth/Documents/Code-practise/Python/general')
print(os.getcwd())
os.rmdir('test')
print(os.getcwd())

# (NB) makedirs create all folder on the specified path, even if they dont exist to ensure the full path exists e.g os.makedirs('C:\\delicious\\walnut\\waffles')

# To make a directory from a Path object, call the mkdir() method, but it can only make one directory at a time; it won’t make several subdirectories at once like os.makedirs()

# The pathlib module provides methods for checking whether a given path is an absolute path and returning the absolute path of a relative path.
# Calling the is_absolute() method on a Path object will return True if it represents an absolute path or False if it represents a relative path.

print(Path.cwd().is_absolute())
print(Path('/Users/kenneth/').is_absolute())
print(Path('Code-practise/Python/general').is_absolute())

# To get an absolute path from a relative path, you can put Path.cwd() / in front of the relative Path object. After all, when we say “relative path,” we almost always mean a path that is relative to the current working directory. This also works for paths other than the cwd.

abs_path = Path.cwd()/Path('Code-practise/Python/general')
print(abs_path.is_absolute())

'''
The os.path module also has some useful functions related to absolute and relative paths:

    Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.

    Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.

    Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.
'''

print('*****')
print(os.path.abspath('.'))
print(os.path.abspath('..'))

path = 'Code-practise/Python/general'
print(os.path.abspath(path))
print(os.path.isabs(path))

start = 'kenneth/Documents/'
print(os.path.relpath(path, start))
print(os.path.relpath(path))

# Given a Path object, you can extract the file path’s different parts as strings using several Path object attributes. These can be useful for constructing new file paths based on existing ones. Parts of a file path include:

# Anchor: root of the file system e.g C:\ or /
# Drive: on Windows the drive is physical hard drive letter e.g C:
# Parent: the folder containing the file i.e the full path from the anchor to folder
# Parents: evaluates to the ancestor folders of a Path object with an integer index
# Name: file name made up of the stem/base_name and the suffix/extension

#(NB) All attribtute above evaluate to a string when extracted from a Path objec, except the parent, which evaluates to anohter Path object

p = Path('/Users/Al/spam.txt')
print(p.anchor)
print(p.parent)
print(p.parents)
print(p.stem)
print(p.suffix, '*******')

wp = Path('C:/Users/Al/spam.txt')
print(wp.anchor)
print(wp.drive)
print(wp.parent)  # This is a POSIX Path object when run on a POSIX system
print(wp.stem)
print(wp.suffix, '##### \n')

# The older os.path module also has similar functions for getting the different parts of a path written in a string value. Calling os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument. Calling os.path.basename(path) will return a string of everything that comes after the last slash in the path argument.

calcFilePath = '/Users/kenneth/Documents/Code-practise/Python/general'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))  # returns a tuple of the path split accordingly

# Also, note that os.path.split() does not take a file path and return a list of strings of each folder. For that, use the split() string method and split on the string in os.sep. (Note that sep is in os, not os.path.) The os.sep variable is set to the correct folder-separating slash for the computer running the program, '\\' on Windows and '/' on macOS and Linux, and splitting on it will return a list of the individual folders.

print(calcFilePath.split(os.sep))

# Finding File Size and Folder Content: Once you have ways of handling file paths, you can then start gathering information about specific files and folders. The os.path module provides functions for finding the size of a file in bytes and the files and folders inside a given folder.

p = '/Users/kenneth/Documents/Code-practise/Python/general'
print(os.listdir(p))  # returns a list of all files in the path directory

# Getting the total size of all file in a folder / folder size
total_size = 0
for file_name in os.listdir(p):
    total_size += os.path.getsize(file_name)

print(total_size)

f = '/Users/kenneth/Documents/Code-practise/Python/general/regular_re.py'
print(os.path.getsize(f))  # returns the file size in bytes

# Glob patterns: If you want to work on specific files, the glob() method is simpler to use than listdir(). Path objects have a glob() method for listing the contents of a folder according to a glob pattern. Glob patterns are like a simplified form of regular expressions often used in command line commands. The glob() method returns a generator object that you’ll need to pass to list() to easily view its contents.

# Use the '*' to match multiple character pattens of a file name
path = Path('/Users/kenneth/Documents/Code-practise/Python/general')
print(list(path.glob('*')))  # returns all file in folder
print('\n', list(path.glob('*.txt')))  # return any file ending with .txt

# list(path.glob('project?.docx')) will return all file that have the name 'project' + any other character e.g project2.docx but not project10.docx as '10' is two characters.

# You can also combine the asterisk and question mark to create even more complex glob expressions e.g list(p.glob('*.?x?') will return files with any name and any three-character extension where the middle character is an 'x'.

# Many Python functions will crash with an error if you supply them with a path that does not exist. Luckily, Path objects have methods to check whether a given path exists and whether it is a file or folder

p = Path(Path('/Users/kenneth/Documents/Code-practise/Python/general'))
print(p.exists())
print(p.is_dir())
print(p.is_file())

# (NB) The older os.path module can accomplish the same task with the os.path.exists(path), os.path.isfile(path), and os.path.isdir(path) functions, which act just like their Path function counterparts.

# READING AND WRITING: Plain text file e.g .txt or script files e.g .py can be read by python scripts and text editors. Their contents are treated as normal strings. Binary files are any other types of file e.g .doc, .pdf, .exe etc and if opened using text editors their contents are scrambled. This is because each bunary file must be handled in a specific way thus need dedicated programs to handle them.

# The pathlib module’s read_text() method returns a string of the full contents of a text file. Its write_text() method creates a new text file (or overwrites an existing one) with the string passed to it.

new_path = Path('spam.txt')
print(new_path.write_text('Hello World'))  # returns the num of char written to a new file
print(new_path.read_text())
print(new_path.write_text('Text changed!'))
print(new_path.read_text())

'''
Keep in mind that these Path object methods only provide basic interactions with files. The more common way of writing to a file involves using the open() function and file objects. There are three steps to reading or writing files in Python:

    1. Call the open() function to return a File object.
    2. Call the read() or write() method on the File object.
    3. Close the file by calling the close() method on the File object.
'''

file_obj1 = open(Path.cwd()/'spam.txt')# open accepting a Path object
print(file_obj1)

# open accepting a string path
file_obj2 = open('/Users/kenneth/Documents/Code-practise/Python/general/test.txt')

# Both above commands open the file in read mode (no writing permitted) by default. Overrirde the default begaviour by adding a seconda argument to specify the mode.

file_obj3 = open(Path.cwd()/'test.txt', 'r')

# Use the file object's read() method to read all file contents line by line or readline() to get a list of lines

# (NB) Except for the last line of the file, each of the string values ends with a newline character \n. A list of strings is often easier to work with than a single large string value.

print(file_obj2.read())
print('\n', file_obj3.readlines())

# To write to a file, you have to open the file in write mode by passing the 'w' argument to open(). This will overrite the file contents with the new contents.
# To add contents to an existing file, open it it append mode using the 'a' argument to open().

# (NB) Both 'w' and 'a' will create a new file, if it does not exist. After reading or writing a file, call the close() method before opening the file again.
print('\n')
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()

print(content)

# Manipulating Binary files using the shelve module: You can save variables in your Python programs to binary shelf files, for example, using the shelve module. This way, your program can restore data to variables from the hard drive. The shelve module will let you add Save and Open features to your program. For example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load them the next time it is run.

# To read and write data using the shelve module, you first import shelve. Call shelve.open() and pass it a filename, and then store the returned shelf value in a variable. You can make changes to the shelf value as if it were a dictionary. When you’re done, call close() on the shelf value. Here, our shelf value is stored in shelfFile. We create a list cats and write shelfFile['cats'] = cats to store the list in shelfFile as a value associated with the key 'cats' (like in a dictionary). Then we call close() on shelfFile. Note that as of Python 3.7, you have to pass the open() shelf method filenames as strings. You can’t pass it Path object.

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

#After running the previous code on Windows, you will see three new files in the current working directory: mydata.bak, mydata.dat, and mydata.dir. On macOS, only a single mydata.db file will be created. These binary files contain the data you stored in your shelf. The format of these binary files is not important; you only need to know what the shelve module does, not how it does it. The module frees you from worrying about how to store your program’s data to a file. Your programs can use the shelve module to later reopen and retrieve the data from these shelf files. Shelf values don’t have to be opened in read or write mode—they can do both once opened

shelfFile = shelve.open('mydata')
print(type(shelfFile))  # check the type of variable storing the shelve file

print(shelfFile['cats'])  # check that our list was correctly stored in the shelve file
shelfFile.close()

# Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf. Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.

print()
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))

print(list(shelfFile.values()))

shelfFile.close()

# Saving variable data to text files using pprint.pformat(): the pprint.pprint() function will “pretty print” the contents of a list or dictionary to the screen, while the pprint.pformat() function will return this same text as a string instead of printing it. Not only is this string formatted to be easy to read, but it is also syntactically correct Python code. Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use. Using pprint.pformat() will give you a string that you can write to a .py file. This file will be your very own module that you can import whenever you want to use the variable stored in it.

import pprint

# Save the cats dict in a mycats.py file
print()
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')

fileObj.close()

# Import the mycats.py file as python module and use it
import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])

# (NB) For most applications, however, saving data using the shelve module is the preferred way to save variables to a file. Only basic data types such as integers, floats, strings, lists, and dictionaries can be written to a file as simple text. File objects, for example, cannot be encoded as text.

print('\n------------- *** DEBUGGING *** --------------------------')
# RAISING EXCEPTIONS: Raising an exception is a way of saying, “Stop running the code in this function and move the program execution to the except statement.” Exceptions are raised with a raise statement and consists of:

    # 1. The raise keyword
    # 2. A call to the Exception() function
    # 3. A string with a helpful error message passed to the Exception() function

# (NB) Often it’s the code that calls the function, rather than the function itself, that knows how to handle an exception. That means you will commonly see a raise statement inside a function and the try and except statements in the code calling the function.


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    # prints the top edge
    print(symbol * width)

    # Prints the sides
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    # prints the bottom edge
    print(symbol * width)

# Driver code attempting to print 4 types of boxes
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)

    except Exception as err:
        print('An exception happened: ' + str(err))

# TRACEBACK: error information produced by python when an error is encountered. It includes the error message, the line number of the line that caused the error, and the sequence of the function calls that led to the error. This sequence of calls is called the CALL STACK. It is displayd when the error is unhandled.

# You can also obtain it as a string by calling traceback.format_exc(). This function is useful if you want the information from an exception’s traceback but also want an except statement to gracefully handle the exception. You will need to import Python’s traceback module before calling this function. For example, instead of crashing your program right when an exception occurs, you can write the traceback information to a text file and keep your program running. You can look at the text file later, when you’re ready to debug your program.

import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try:
    spam()

except:
    errofile = open('errofile.txt', 'w')
    errofile.write(traceback.format_exc())
    errofile.close()

    print('\nThe traceback info was written to errorfile.txt')

# ASSERTIONS: are sanity check to make sure your code isn’t doing something obviously wrong. These sanity checks are performed by assert statements. If the sanity check fails, then an AssertionError exception is raised. In code, an assert statement consists of the following:

# The assert keyword
    # 1. A condition (that is, an expression that evaluates to True or False)
    # 2. A comma
    # 3. A string to display when the condition is False

# An assert statement says, “I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program.” These are used to detect bugs during development and should not be used in production code.

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
assert ages[0] <= ages[-1]  # Does nothing as result is True
# assert ages[0] >= ages[-1]  # Raises AssertError as result is False

# (NB) Assertions should also not replce comprehensive tests

print('\n------------- *** WEB SCRAPING *** --------------------------')
# Web scraping is the term for using a program to download and process content from the web.

# The webbrowser module for opening a URL in a webrowser e.g a Google maps address

def map_address():
    import webbrowser, sys, pyperclip

    if len(sys.argv) > 1:
        address = ''.join(sys.argv[1:])

    else:
        address = pyperclip.paste()

    webbrowser.open(f'https://www.google.com/maps/place/{address}')

# map_address()

# The requests module lets you easily download files from the web without having to worry about complicated issues such as network errors, connection problems, and data compression.

def download_file():
    import requests

    response_obj = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    response_obj.raise_for_status() # raises HTTPError if download was not successfull

    return response_obj

# Saving downloaded files: Even if the page is in plaintext (such as the Romeo and Juliet text you downloaded earlier), you need to write binary data instead of text data in order to maintain the Unicode encoding of the text. This is achieved by opening the file in write bnary mode:

    # open('file', 'wb')

def save_file_download():
    res_obj = download_file()
    file = open('Romeo_Juliet_download.txt', 'wb')

    for file_chunk in res_obj.iter_content(10000):
        file.write(file_chunk)

    file.close()

save_file_download()

# Using the Beautiful Soup module (bs4) for extracting information from an HTML page.
# (pip install bs4)
# The bs4.BeautifulSoup() function needs to be called with a string containing the HTML it will parse. The bs4.BeautifulSoup() function returns a BeautifulSoup object.

def bs4_demo():
    import requests, bs4

    res = requests.get('https://nostarch.com')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(type(noStarchSoup))

# bs4_demo()

# This code uses requests.get() to download the main page from the No Starch Press website and then passes the text attribute of the response to bs4.BeautifulSoup(). The BeautifulSoup object that it returns is stored in a variable named noStarchSoup. You can also load an HTML file from your hard drive by passing a File object to bs4.BeautifulSoup() along with a second argument that tells Beautiful Soup which parser to use to analyze the HTML.

# The 'html.parser' parser used here comes with Python. However, you can use the faster 'lxml' parser if you install the third-party lxml module (pip install lxml). Forgetting to include this second argument will result in a UserWarning: No parser was explicitly specified warning. Once you have a BeautifulSoup object, you can use its methods to locate specific parts of an HTML document.

# Find elements in HTML docs using the bs4 select() method by passing a string of a CSS selector for the element you are looking for. Selectors are like regular expressions: they specify a pattern to look for—in this case, in HTML pages instead of general text strings. CSS selector syntax: https://nostarch.com/automatestuff2/. The various selector patterns can be combined to make sophisticated matches.

# Instead of writing the selector yourself, you can also right-click on the element in your browser and select Inspect Element. When the browser’s developer console opens, right-click on the element’s HTML and select Copy ▸ CSS Selector.

# The select() method will return a list of Tag objects, which is how Beautiful Soup represents an HTML element. The list will contain one Tag object for every match in the BeautifulSoup object’s HTML. Tag values can be passed to the str() function to show the HTML tags they represent. Tag values also have an attrs attribute that shows all the HTML attributes of the tag as a dictionary.

def parse_example_html():
    import bs4

    e_file = open('example.html')
    e_soup = bs4.BeautifulSoup(e_file.read(), 'html.parser')
    tag_obj = e_soup.select('#author') # all tags with attr id='author

    e_file.close()

    print(f'# of tags: {len(tag_obj)}, tags obj type: {type(tag_obj[0])}, \
        HTML tag type: {str(tag_obj[0])}, tag innerHTML: {tag_obj[0].getText()}, \
        all tag attributes: {tag_obj[0].attrs}')

# parse_example_html()

# The get() method for Tag objects makes it simple to access attribute values from an element. The method is passed a string of an attribute name and returns that attribute’s value.

def parse_example_html2():
    import bs4

    soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
    spanElem = soup.select('span')[0]

    print(str(spanElem))

    print(spanElem.get('id'))

    print(spanElem.get('some_nonexistent_addr') == None)

    print(spanElem.attrs)

parse_example_html2()