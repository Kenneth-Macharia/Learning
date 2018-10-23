#Decorators which are @staticmethods or @classmethods and are simply funtions that are called before other functions.
#Decorators modify the function being decorated.
import functools  #Python library necessary to us Decorators

''' Creating a decorated '''
def my_decorator(decorated_func):
    @functools.wraps(decorated_func)
    def function_that_runs_decorated_func():
        print 'This is code that runs in the decorator'
        decorated_func()  #Calls the decorated function, if not called the actual function never runs.
        print 'This is code that runs after the decorator'
    return function_that_runs_decorated_func  #Value returned that replaces the decorated function.

''' Using the decorator created above '''
@my_decorator
def decorated_func():
    print 'This is code in the decorated function'

#decorated_func()


''' Creating a decorator with arguments '''
def decorator_with_args(decorator_arg):
    def my_decorator(decorated_func):
        @functools.wraps(decorated_func)
        def function_that_runs_decorated_func(*args, **kwargs):
            print 'This is code that runs in the decorator'

            if decorator_arg == 56:
                print 'Not running decorated_func'
            else:
                decorated_func(*args, **kwargs)

            print 'This is code that runs after the decorator'
        return function_that_runs_decorated_func
    return my_decorator

''' Using the decorator with arguments '''
@decorator_with_args(57)
def decorated_func(x, y):
    print x + y

#decorated_func(4, 5)
