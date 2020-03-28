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
