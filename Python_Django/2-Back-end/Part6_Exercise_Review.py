#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
s[0]

# 'o'
s[-1]

# 'djan'
s[:4]

# 'jan'
s[1:4]

# 'go'
s[4:]

# Bonus: Use indexing to reverse the string
s[::]
s[::-1]

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]

# Reassign "hello" to be "goodbye"
l[2][2] = 'goodbye'

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
d1['simple_key']

d2 = {'k1':{'k2':'hello'}}
d2['k1']['k2']

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3['k1'][0]['nest_key'][1][0]

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
set(mylist)

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {b} and he is {a} years old".format(a = age, b = name))
print("Hello my dog's name is {} and he is {} years old".format(name, age))

# Tuple unpacking
my_pairs = [(1,2), (3,4), (5,6)]

for tup1, tup2 in my_pairs:
    print(tup1, tup2)

    print(tup1)
    print(tup2)

    print(tup2)
    print(tup1)
    
