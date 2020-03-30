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


# RAW STRINGS: achieved by preceesing a string with 'r' then all escape charaters are ignored and trated as part of the string e.g:

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
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

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

# Non-greedy matches are specified using the '?' (Note this is stil used for optinal matching, which are not related)
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

# There are many Shorthand Character Classes such as \d standing for the regex ((0|1|2|3|4|5|6|7|8|9)) available (See Django notes + Python documentation). The character class [0-5] will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5).
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
# SWhat if you want to use re.VERBOSE to write comments in your regular expression but also want to use re.IGNORECASE to ignore capitalization? Unfortunately, the re.compile() function takes only a single value as its second argument. You can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|), which in this context is known as the bitwise or operator.
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
