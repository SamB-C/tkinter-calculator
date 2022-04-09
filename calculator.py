from tkinter import *
from eval_commands import button_clicked

def main():

    root = Tk()
    root.title('Simple Calculator')

    result = Entry(root, width=30, borderwidth=5)
    result.grid(row=0, column=0, columnspan=4)

    regular_button_design = {'width': 10, 'height': 3}


    #CREATE BUTTONS
    # Returns the function to be passed in as a commmand to the Buttons
    def get_command(item):
        print('Getting command: ' + item, '\tType:', type(item))
        return lambda: button_clicked(item, result)

    # Create Brackets and Clear (Row 1)
    button_open_brackets = Button(root, text='(', command=get_command('('), **regular_button_design)
    button_close_brackets = Button(root, text=')', command=get_command(')'), **regular_button_design)
    button_open_brackets.grid(row=1, column=0)
    button_close_brackets.grid(row=1, column=1)

    button_clear = Button(root, text='CE', command=get_command('CE'), **regular_button_design)
    button_clear.grid(row=1, column=3)

    button_convert_percentage = Button(root, text='%', command=get_command('%'), **regular_button_design)
    button_convert_percentage.grid(row=1, column=2)


    # Create and position numbers 0 - 9
    numbers = [Button(root, text=i, command=get_command(str(i)), **regular_button_design) for i in range(1, 10)]

    for index, number_button in enumerate(numbers[::-1]):
        column = 2 - (index % 3)
        row = (index // 3) + 2
        number_button.grid(row=row, column=column)
    numbers.insert(0, Button(root, text='0', **regular_button_design, command=get_command('0')))
    numbers[0].grid(row=5, column=0)



    # Create buttons for = and . (Row 5)
    button_equals = Button(root, text='=', **regular_button_design, command=get_command('='))
    button_equals.grid(row=5, column=2,)

    button_floating_point = Button(root, text='.', command=get_command('.'), **regular_button_design)
    button_floating_point.grid(row=5, column=1)


    # Create + - * / (Column 3)
    button_add = Button(root, text='+', command=get_command('+'), **regular_button_design)
    button_subtract = Button(root, text='-', command=get_command('-'), **regular_button_design)
    button_multiply = Button(root, text='*', command=get_command('*'), **regular_button_design)
    button_divide = Button(root, text='/', command=get_command('/'), **regular_button_design)
    button_add.grid(row=2, column=3)
    button_subtract.grid(row=3, column=3)
    button_multiply.grid(row=4, column=3)
    button_divide.grid(row=5, column=3)


    root.mainloop()

if __name__ == '__main__':
    main()