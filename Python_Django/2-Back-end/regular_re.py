import re

# pattern to search for
patterns = ['term1', 'term2', 'term3', 'term']

# string to search pattern in
text = 'This is a string with term1, and not the other term'

# for pattern in patterns:
#     print('I am searching for: {}'.format(pattern)) # code to execute each tiem a match is found

# Using re module functionality to perform the search 
for pattern in patterns:
    print('I am searching for: {}'.format(pattern))

    if re.search(pattern, text):
        print('MATCH FOUND')
    else:
        print('NO MATCH!')

# re.search() returns special regular expressions object <class '_sre.SRE_Match'> which contains more than the booleanes of the search, it contains other details e.g where in the text the match was found e.g: at what index withn the string, using the start() method

match_info = re.search(pattern, text).start()
print(match_info)

# You can also split the text, returns a list of the split part of the string
split_term = '@'
email = 'user@email.com'

print(re.split(split_term, email))

# Using re to find all instance of a pattern, returning a list of of all non-overlapping matches
print(re.findall('match', 'This text has two match strings that need to find match for'))

# Using metacharacters to find repetition within
def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('Searching for pattern: %s') %pattern
        print(re.findall(pat, phrase))
        print('\n') # print a new line after every search pass

# Finding patterns
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_pattern = ['sd*'] # returns a list with all patterns featuring 's' and 'd' repeated zero or more times
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd+'] # returns a list with all patterns featuring 's' and 'd' repeated one or more times
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd?'] # returns a list with all patterns featuring 's' and 'd' repeated zero or once
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd{3}'] # returns a list with all patterns featuring 's' and 'd' a specific number of times
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd{1,3}'] # returns a list with all patterns featuring 's' and 'd' a specific number of times or another specific number of times
multi_re_find(test_pattern, test_phrase)

test_pattern = ['s[sd]+'] # returns a list with all patterns featuring 's' and followed by either 1 or more 's' or 'd'.
multi_re_find(test_pattern, test_phrase)

# Exclusions using the 'carrot' ^ symbol
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_pattern = ['[^!.?]+'] # Splits the string where the punctuations appear one or more times
multi_re_find(test_pattern, test_phrase)

# Sequences of lower case letters: ['[a-z]+'], uppercase ['[A-Z]+'], both upper and lower case ['[a-zA-Z]+'], one upper followed by one or more lower case ['[A-Z][a-z]+'] etc

# Finding escape characters, which in python are prefixed by '\'. However the '\' must itself be escaped in a normal string, which is done by making a literal value using 'r'. 

test_phrase = 'This is a string890! But it has numbers 22. How can we #remove 12them?'
test_pattern = [r'\d+'] # returns sequences of one or more digits
multi_re_find(test_pattern, test_phrase)

test_phrase = 'This is a string890! But it has numbers 22. How can we #remove 12them?'
test_pattern = [r'\s+'] # returns sequences of one or more spaces
multi_re_find(test_pattern, test_phrase)

test_phrase = 'This is a string890! But it has numbers 22. How can we #remove 12them?'
test_pattern = [r'\D+'] # returns sequences of one or more non-digits
multi_re_find(test_pattern, test_phrase)

test_phrase = 'This is a string890! But it has numbers 22. How can we #remove 12them?'
test_pattern = [r'\S+'] # returns sequences of one or more non-spaces
multi_re_find(test_pattern, test_phrase)

test_phrase = 'This is a string890! But it has numbers 22. How can we #remove 12them?'
test_pattern = [r'\w+'] # returns sequences of one or more alphanumerics
multi_re_find(test_pattern, test_phrase)

test_phrase = 'This is a string890! But it has numbers 22. How can we #remove 12them?'
test_pattern = [r'\W+'] # returns sequences of one or more non-alphanumeric
multi_re_find(test_pattern, test_phrase)


