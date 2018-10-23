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
# condition = True
# if condition == True:
#     print ('continue')
#
# #Can also be:
# if condition:
#     print ('continue')

#Flow control coding exercise
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_numbers():
    return list(filter(lambda x: x%2 == 0, nums))
    return [x for x in nums if x%2 == 0]

#print(even_numbers())
# def user_menu(choice):
#     if choice == 'a':
#         return 'Add'
#     elif choice == 'q':
#         return 'quit'

# user_wants = True
# while user_wants == True:
#     print(10)
#     input = raw_input('Print number again? (y/n)')
#     if input == 'n':
#         user_wants = False

def user_menu():
    choice = 'a'
    while choice == 'a':
        choice = raw_input('Enter a choice... {a/q}')
        if choice == 'a':
            print 'Add'
        elif choice == 'q':
            print 'quit'

#user_menu()

#Who do you know excercise
def who_do_you_know():
    ''' Ask user names of people they know
        Split the string into a list
        Return the list '''

    names_string = raw_input('Enter comma separated names of people you know..')
    names_list_without_spaces = [name.strip() for name in names_string.split()]
    return ask_user(names_list_without_spaces)

def ask_user(names_list):
    ''' Ask the user for a name
        See if the name is in the list of people they know
        Print out that they know that person '''

    user_name = raw_input('Enter a name....')
    if user_name in names_list:
        print 'You know {}.'.format(user_name)
    else:
        print 'You dont know {}.'.format(user_name)

#who_do_you_know()

# people = ['Rolf ', 'JOHN', ' gREg']
# normialized_people = [person.strip().lower() for person in people]
#print(normialized_people)

''' dict are key-value sets, unique(by key) & unordered '''
lottery_players = [
{
    'name':'Rolf', 'numbers':(23, 56, 89, 78)
},
{
    'name':'Anna', 'numbers':[56, 89, 52, 10]
}
]

print(sum(lottery_players[0]['numbers']))
print((lottery_players[1]['numbers'])[1] + (lottery_players[1]['numbers'])[3])

lottery_players[1]['name'] = 'Greg'
print(lottery_players[1])

lottery_players[1]['numbers'][2] = 22
print(lottery_players[1]['numbers'])

lottery_players[0]['numbers'] = (lottery_players[1]['numbers'])
print(lottery_players[0]['numbers'])
