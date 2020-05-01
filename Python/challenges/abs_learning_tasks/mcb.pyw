'''
A re-write of the orignal multi-clipboard script. The user will now be able to save new strings to load to the clipboard without having to modify the source code. We’ll name this new program mcb.pyw (since “mcb” is shorter to type than “multi-clipboard”). The .pyw extension means that Python won’t show a Terminal window when it runs this program.

It will save each piece of clipboard text under a keyword. For example, when you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam. This text can later be loaded to the clipboard again by running py mcb.pyw spam. And if the user forgets what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard.

Here’s what the program does:

    1. The command line argument for the keyword is checked.
    2. If the argument is save, then the clipboard contents are saved to the keyword.
    3. If the argument is list, then all the keywords are copied to the clipboard.
    4. Otherwise, the text for the keyword is copied to the clipboard.
'''

# USAGE:
    # python mcb.pyw save <keyword> - Saves clipboard to keyword.
    # python mcb.pyw <keyword> - Loads keyword to clipboard.
    # python mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # TODO: List keywords or load content based of the keyword supplied
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()