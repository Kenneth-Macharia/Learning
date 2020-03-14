# Nested functions and assigning funcs to variables

def hello(name='Ken'):
	print('Ran hello')

	def greet():
		return 'Ran greet'

		def welcome():
			return 'Ran welcome'

	if name == 'Ken':
		return greet
	else:
		return welcome


#x = hello()  # Run the hello func and stores its return value in x but does not display the return value. The func 'greet' is returned because the value of name='Ken'

#x() # Runs the func stored inside of x, does not display its string, need print()
#print(x())  # Displays the return string of the func 'greet' inside x

# Passing functions as arguments to other functions

def hello():
	return 'Ran hello'

def other(func):
	print('Ran other')
	print(func)
	print(func())

#other(hello)  # Running other and passing the hello func as args

# Using decorators:

# Method 1:
def modifier_func(func):

	# Define the wrapper function inside the decorator
	def wrap_func():
		print('Code to run before un_decorated function')
		func() # Function passed in as argument
		print('Code to run after un_decorated function')

	return wrap_func

def un_decorated_func():
	print('Ran Undecorated func')

decorator_returns = modifier_func(un_decorated_func)  # Decorator returns the func 'wrap_func'
decorator_returns() # Run the 'wrap_func' returned

print('\n--------------------------------')

# Method 2:
def decorator(func):

	def wrap_func():
		print('Code to run before decorated function')
		func() # Function passed in as argument
		print('Code to run after decorated function')

	return wrap_func

@decorator
def decorated_func():
	print('Ran decorated func')

decorated_func()
