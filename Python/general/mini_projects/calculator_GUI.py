'''
A simple calculator allowing the user to enter a number in a text field, and either add it to or subtract it from a running total, which we will display.

https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

'''
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title('Calculator')

        self.total = 0
        self.entered_number = 0
        self.operation = ''

        self.total_label_text = IntVar()    # Setting label texts requires special object
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text='Total')

        vcmd = master.register(self.validate)   # wrap the command
        self.entry = Entry(master, validate='key', validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text='+', command=lambda:self.update('add'))
        self.subtract_button = Button(
            master, text='-', command=lambda:self.update('subtract'))
        self.equals_button = Button(
            master, text='=', command=lambda:self.update('equals'))
        self.reset_button = Button(
            master, text='Reset', command=lambda:self.update('reset'))

        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.equals_button.grid(row=2, column=2)
        self.reset_button.grid(row=3, column=2, sticky=E)

    def validate(self, new_text):
        ''' Checks that inputs are type int '''

        if not new_text:    # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        ''' Changes the total label showing calculation results based on the action performed '''

        if method == 'equals':
            if self.operation == 'add':
                self.total += self.entered_number
            elif self.operation == 'subtract':
                self.total -= self.entered_number
            elif self.operation == 'reset':
                self.total = 0
                self.total_label_text.set(self.total)

            self.total_label_text.set(self.total)
            self.entry.delete(0, END)
            self.operation = ''

        else:
            self.operation = method
            self.entry.delete(0, END)


# Run the program
root = Tk()
my_gui = Calculator(root)
root.mainloop()