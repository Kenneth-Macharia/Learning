''' Object in python '''
class Student(object):

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average_mark(self):
        return sum(self.marks)/len(self.marks)

    def going_to_school(self):
        print('I am going to {}.'.format(self.school))

# anna = Student('Anna', 'MIT')
# anna.marks.append(56)
# anna.marks.append(74)
# anna.marks.append(78)
# print(anna.name, anna.average_mark())
# anna.going_to_school()

''' class & static methods '''
class Store(object):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        new_item = {'name':name, 'price':price}
        self.items.append(new_item)

    def get_items(self):
        return [items for items in self.items]

    def stock_price(self):
        return sum([items['price'] for items in self.items])

    @classmethod
    def franchise(cls, store):
        return store + ' - franchise'

    @staticmethod
    def store_details(store):
        return '{} store total stock is {}'.format(store, int(store2.stock_price()))

# store1 = Store('Tuskys')
# store1.add_item('sugar',100)
# store1.add_item('salt',30)
# store1.add_item('bread',50)
# print(store1.name, store1.get_items(), store1.stock_price())

# store2 = Store('Tuskys')
# store2.add_item('sugar',100)
# store2.add_item('salt',30)
# store2.add_item('bread',50)
# print(Store.franchise('Nakumatt'))
# print(Store.store_details('Naivas'))

''' Inheritance (Why to use class or static methods)'''
class Student(object):

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average_mark(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs) #Implement args

# anna = Student('Anna', 'MIT')
# friend = anna.friend('Peter')
# print (friend.name)
# print (friend.school)

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super(WorkingStudent, self).__init__(name, school)
        self.salary = salary
        self.job_title = job_title

# tom = WorkingStudent('Tom', 'Oxford', 20.00, 'DevOps') #args only
# print(tom.name, tom.school, tom.salary)
# friend = WorkingStudent.friend(tom, 'greg', 19.00, job_title='Dev') #args & kwargs
# print(friend.name, friend.school, friend.salary, friend.job_title)


''' *Args (positional function arguments) & **Kwargs (keyword function arguments) '''

#If you have a fucntion:
def my_list_addition(list_args):
    return sum(list_args)

#Must be called and give in a list :
my_list_addition([3, 5, 6, 9])

#A simplified version:
def simple_list_addition(*args):
    return sum(args)

#And call it as:
simple_list_addition(3, 5, 6, 9, 7)


#If you also have a fucntion:
def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

#what_are_kwargs(12,36,45)  #args are a tuple (), kwargs are a set {}
#what_are_kwargs(name='Jose', location='UK')
#what_are_kwargs(56, name='Jose') # args come first, then kwargs always

#Functions as parameters

def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

#print(methodception(add_two_numbers))

#lambda fucntions are anonymous funcions i.e:
#print(methodception(lambda:35 + 77))

#Declarative / functinal programming
#if you hae a list and want to return odd number only:

my_list = [12, 45, 6, 89, 102, 1]

#use Python built in function (filter) + a lambda function for the condition:
#Filter takes a function & an iterable

#print(list(filter(lambda x: x%2!=0, my_list )))

#List comprehenion equivalent:
#print([x for x in my_list if x%2!=0])

#Filter is used in other languages e.g. Js, hence more familiar
#List comprehenions are uniques to Python, hence less familiar.

#More lambda examples

#print((lambda x: x * 3)(5))
def f(x):
    return x * 3
#print f(5)
