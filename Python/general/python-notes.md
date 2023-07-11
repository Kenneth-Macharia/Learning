# Intro

_ALSO REFER TO THE PART.PY FILES FOR MORE NOTES AND EXPLANATIONS TOGETHER WITH DEMOS_

- Python is a DYNAMIC PROGRAMMING LANGUAGE because you dont need to declare variable type before assignment, as opposed to STATIC PROGRAMMING languages, where variable types have to be known at pre-run time.
<https://stackoverflow.com/questions/20563433/difference-between-static-and-dynamic-programming-languages>

## Strings

- Negative indexing: string[-1] # returns the last char, and goes on till index 0 to get the corresponding letter.
- String slicing: string[2:] # returns all chars from index 2 to the end, string[:3] # returns all chars from index 0 to index 2, string[2:5] # returns all chars from index 2 upto index 4, string[::] / string[:] # returns all character, string[::3] # skips 3 three letters at a time, string[::-1] # returns the string reversed.
- Strings are IMMUTABLE, no re-assignment once created, thus even l = l + 'p' creates a new string   object, rather than appending to the original object.

_STRING INTERPOLATION: the process of substituting string within a string with other string, including arithmetic computation_

    https://www.programiz.com/python-programming/string-interpolation

## Lists

- Support slicing & -ve indexing just like with strings, since they are all array sequences.
- list1.extend(list2) adds list2 items to the end of list1, unlike list1.append(list2) which will add list2 as an item at the end of list1.
- list.pop(index), will pop the item in the specified index location.
- There is a list.sort()

## Booleans (True (1), False (0))

## Tuples

- Immutable list-like structure but declared () unlike [] for lists.
- TUPLE UNPACKING is multiple variable assignment

## Sets

- UNORDERED collection of UNIQUE elements.
- Declare using set(), then use methods to manipulate e.g set.add(element).

    `unique_list = set([1,2,3,2,1,4,3,4,2,5,5]) # returns set(1,2,3,4,5)`

## Range

- Can be used to generate numbers between a range e.g. list(range(0, 5)), returns a list of items between 0 and 4, list(range(0, 20, 2)) will generate a list of even numbers between 0 and 19 (2 is a step argument).
- Ranges are beneficial when the numbers generated need not be saved in memory i.e to a variable, e.g when iterating through some range of numbers work on something other than the number range.

## Functions

- Default function parameters:

    def my_function( param1 = 'default' );

- Lambda expresion == anonymous functions: where we dont have to define a function, if we will use it once and inside of another:

        ''' Suppose we have the below code: '''

            list_of_nums = [1,2,3,4,5,6,7,8,9]

            def is_even(num):
            ''' returns true if a number passed to it is even '''

                return num_list%2 == 0

- Using the filter generater to get all even number from a list, supply to it, the list and a condition to check that a number is even.

    `even_numbers = list(filter(is_even, list_of_nums)`

- All the above can be replaced with:

    `even_numbers = list(filter(lambda num:num_list%2 == 0, list_of_nums))`

## Scope

- Python uses the namespace system to make sure that all names declared in a program are unique and can be reached without any conflict.
- Name spaces are:

    1. Local namespace: includes name declared within a function (def or lambda) and only last until a return is done.
    2. Global namespace: includes names from imported modules and lasts until the end of the script/ program.
    3. Built-in namespace: includes built-in fucntins and exception names.

- Scope defines the parts fo the program that a name can be used without a prefix e.g math.log10() or cmath.log10() and these include:

    1. Local scope - innermost scope defining names available within the current function.
    2. Scope of all enclosing functions: sesrch starts from the nearest function moving outwards, for nested structures.
    3. Module scope: contains global names for the current module and all local names defined with the 'global' keyword.
    4. Outter scope containing all built-in names, and used to find referenced names.

- If a name is not found in any of the scopes above a 'NameError' exception is raised.

_If you define a global variable inside a local namespace with a similar name as global namespace variable and re-assign its value, the reference of the globally defined variable is moved to the locally defined global variable_

<https://code.tutsplus.com/tutorials/what-are-python-namespaces-and-why-are-they-needed--cms-28598>

- Working with the built-in namespace scope:

    1. Method 1 for importing names: 'from module1 import *, imports all the names from that module, and is both inefficent and risky as you will be importing names that will not be used. Also there is high risk of name conflict due to the high name population and if another module with similar names is imported, their names overwrite any similar names of the first unexplicit import.

    2. Method 2: from module1 import nameA, nameB: only imports the two names explicitly mentioned. Also, any name in the local module namespace, having similar names with the explicitly imported names will overwrite the imported names.

    3. Method 3: import module, the safest and recommend module import method allowing prefixing of imported names with the imported module name to prevent conflict with the local module namespace e.g math.random()

<https://www.pythonmorsels.com/4-ways-import-module-python/>

- Locals() internal function returns a dict of all local scope variables and globals() returns all globals scope variables.

## OOP

- Everything in python is an object, thus inherits from the object class.
- Check the type or which class an object belongs to by using the 'type()' method.
- OOP enables the creation of object and define properties and methods that facilitate efficient interacton with said objects.
- Classes are used to create the objects and are bluepints defining the architecture of an object. From the classes, we can create instances of the class, and instances are basically objects created based on the specifications of a class e.g.

    class SomeClass ():  // creates a class called SomeClass.
    class_object = SomeClass(att1 = att_value, att2 = att_value)  // Instantiate the class, method1
    class_object = SomeClass(att_value, att_value)  // Instantiate the class, method2

_instantiate a class with a default attribute value: `__int__(self, att1 = default_value)`_

- Define class attributes outside the class __init__ constructor and without the 'self' keyword.

## Inheritance

- Python class special methods are all wrapped by `__ __` and must take the _self_ keyword. They make class objects self-sufficient and encourage the priciples of OOP e.g abstraction and encapsulation. Examples include:

        __str__ which returns the string representations of a classes object, more useful to end users.
        __len__ which can be used to define some length attribute of a class e.g lists e.g. len(object_name)
        __del__ is a finalizer called when an object is garbage collected, after all references to the object are deleted.
        __getitem__ used for accessing list items, dictionary entries, array elements etc
        __repr__   returns a printable representation of the object, more useful to developers.

- These special/ magic/ dunder methods enables emulation of built-in types in your programs and make code more pythonic. The design allowing use of these special methods is called the python data model.
<https://dbader.org/blog/python-dunder-methods>

## Errors and Exceptions

- Errors raised take the form: '<type_of_error>Error' e.g SyntaxError, NameError, IOError etc
- Use of try, except, finally blocks to catch anticipated errors and continue with code execution when errors arise in code.

        Illustrations:
            1. Catch specific errors:

            try: #Attempt to write to file
                f = open('simple.txt', 'r')
                f.write('Writing to file')

            except IOError: #Catch exception and execute catch code
                print('Error, can't wirte to file')

            finally: #Code to execute whether or not error is raised
                f.close()

            else: #Code to execute if no error is raised
                print('Success')

            2. Since it may be hard to anticipate all errors or know the exact type of error to anticipate, use a general exception catch block:

            try: #Attempt to write to file
                f = open('simple.txt', 'r')
                f.write('Writing to file')

            except: #Catch exception and execute catch code
                print('Error, can't wirte to file')

            finally: #Code to execute whether or not error is raised
                f.close()

## Regex

- Used to search for patterns in strings, from the 're' module.
- Searches using literals (values) and metacharacters (wildcard-like symbols):

    1. Part8_Regular_Expressions.py
    2. <https://www.analyticsvidhya.com/blog/2015/06/regular-expression-python/>

- Regular expresions (regex) have numerous applications including data cleaning and offer a super convienient way to parse strings.

_DEMOS: regular_ _re.py_

## Modules and Packages

- Modules are other .py files that are imported into the current project files to include their code in the importing file.
- Import a module by the import keyword at the top of the file in which they are required followed by the file name to import without the .py extension.
- To use any of the members in the imported module e.g variable or functions: module.member/ member()
- When modules are imported, a __pycache__ folder is included in the project root, which contains .pyc files of all imported modules' compiled bytcode to enable their fast execution.
- You can also import as follows: import my_module as mm (shortened name), then use the module as:
    mm.member / mm.member()
- Packages are a collection of modules ie many .py files and are mostly used as follows:
    from my_package import my_module

_See 7. SCOPE above for more on importing dos and donts_

## Name and Main

- __name__ is an internal variable that is set to the current file in which it is in, at runtime.
- '__main__' is the file that has been invoked by the interpreter ie. python file.py (in this case file.py is  __main__)
- This python logic is used to differentiate whether the current file is being run as an import or is the actual file being run and based off this decision, some task can be done or not.
- Unlike languages like Java, Python does not have a main() method that gets executed first, in Python main() is all runnable code at the top-level indent 0, meaning code that runs without being invoked.
- Thus if you specify:

    if __name__ == "__main__":
        main()
    Means that all top indent level code will run, if the current file is directly run by the interpreter.

    if __name__ == "__main__":
        some_funtion()
    Means that some_funtion will specify run first, when the current file is directly run by the interpreter.

- The above two also mean that if the current file/module is imported, then the main () code or some_funtion will not run automatically, until when specifically invoked in then importing module.

# Decorators

- Are functions that modify the functionality of other functions, thereby making your code shorter and more pythonic.

- You can assign labels/ variables to functions e.g:

        def hello(name='Ken'):
            print ("Hello , name)

        someV = hello  # Assign function inside a variable
        print(someV())  # Call the variable as a function

- You can also nest funcions:

        def hello(name='Ken'):
            print ("Hello , name)

            def greet():
                return some_vaue

                def welcome():
                    return some_value2

- Possible calls:

            greet()
            welcome()

_greet() and welcome() cant be called here as they are not in this scope_

- Possible calls:

        hello()

- You can also pass in functions as arguments to other functions using the 'func' keyword.

- The purpose of decorators is to ease the process of modifying a functions behaviour by assigning it to another function that does the modification and and returns the modified function.

- To create a decorator:

    1. Define the decorator function that takes a functions as an argument
    2. Inside the decorator, define a wrap_func which executes some code plus calls the function that needs modifying.
    3. Return the wrap_func inside the decorator functions (NOT run it)

- The deocrator can be use in two ways:

    1. Run the decorator and assign the function needing modifying to it
    2. The pythonic way: add an @decorator_function ontop of the function needing modifying, then run the function the normal way.

_Demo in decorator.py_
