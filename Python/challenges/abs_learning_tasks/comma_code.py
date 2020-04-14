'''
COMMA CODE
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. Your function should be able to work with any list value passed to it.

Be sure to test the case where an empty list [] is passed to your function.

Input: ['apples', 'bananas', 'tofu', 'cats']
Output: 'apples, bananas, tofu, and cats'

'''

def comma_code(list):
    if len(list) > 0:
        new_str = ''

        for word in list:
            if list.index(word) != len(list) - 1:
                new_str += word + ', '
            else:
                new_str += 'and ' + word

    return new_str

print(comma_code(['apples', 'bananas', 'tofu', 'cats']))