lists = [2, 3, 4, 5] #ordered (creation order) & mutable
tuple = (2, 3, 4, 5) #Immutable - can't be changed via code.
set = {2, 3, 4, 5} #unique unordered item collections.

#working with tuples
new_tuple = tuple + (6,)

#working with sets
set.add(6)

set_one = {1, 5, 10, 2}
set_two = {3, 5, 10, 13, 4}

#Getting set intersection i.e. common items
# print (set_one.intersection(set_two))
# print ('__________________________')

#Adding sets together i.e. uniques items only
# print (set_one.union(set_two))
# print ('__________________________')

#Getting set difference i.e Elements of set_one not elements of set_two
# print (set_one.difference(set_two))
# print (set_two.difference(set_one))

''' Run a different python version > python3.5 <file to run> '''

''' For loops for looping through an iterable '''
''' WHile loop for looping whilea condition is true or false '''

''' If statements '''
condition = True
if condition == True:
    print ('continue')

#Can also be:
if condition:
    print ('continue')
