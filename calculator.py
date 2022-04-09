from tkinter import *

root = Tk()
root.title('Simple Calculator')

result = Entry(root, width=30, borderwidth=5)
result.grid(row=0, column=0, columnspan=4)

regular_button_design = {'width': 10, 'height': 3}


#CALCULATING
# Handles calculator inputs
expression = []
display_expression = []
current = []

def evaluate(expression_list):
    total = float(expression_list[0])
    current_operation = ''
    for expression_section in expression_list[1:]:
        if expression_section in ['+', '-', '*', '/']:
            current_operation = expression_section
        elif expression_section == '%':
            total = total / 100
        elif expression_section:
            expression_section = float(expression_section)
            if current_operation == '+':
                total += expression_section
            elif current_operation == '-':
                total -= expression_section
            elif current_operation == '*':
                total *= expression_section
            elif current_operation == '/':
                total /= expression_section
    if total % 1 == 0:
        total = int(total)
    return total



def button_click(number):
    current.append(str(number))
    display(''.join(display_expression)+''.join(current))

def clear():
    result.delete(0, END)
    current.clear()
    expression.clear()
    display_expression.clear()

def button_equal():
    expression.append(''.join(current))
    display_expression.append(''.join(current))
    total = evaluate(expression)
    clear()
    result.insert(0, total)
    current.extend(list(str(total)))

def button_operation(operation):
    expression.extend([''.join(current), operation])
    display_expression.extend([''.join(current), operation])
    display(''.join(display_expression))
    current.clear()

def open_bracket():
    if expression:
        if expression[-1] not in ['+', '-', '*', '/']:
            expression.append(''.join(current))
            current.clear()
            display_expression.append(expression[-1])
            expression.append('*')
    elif current:
        expression.append(''.join(current))
        current.clear()
        display_expression.append(expression[-1])
        expression.append('*')
    expression.append('(')
    display_expression.append('(')
    display(''.join(display_expression))

def close_bracket():
    expression.extend([''.join(current), ')'])
    display_expression.extend([''.join(current), ')'])
    display(''.join(display_expression))
    evaluation_start = len(expression) - expression[::-1].index('(') - 1
    sub_expression = expression[evaluation_start + 1:-1]
    [expression.pop() for i in range(len(sub_expression)+2)]
    evaluated_sub_expression = evaluate(sub_expression)
    current.clear()
    expression.append(str(evaluated_sub_expression))



def display(message):
    result.delete(0, END)
    result.insert(0, message)

#CREATE BUTTONS
# Returns the function to be passed in as a commmand to the Buttons
def get_number(num):
    return lambda: button_click(num)

# Create Brackets and Clear (Row 1)
button_open_brackets = Button(root, text='(', command=open_bracket, **regular_button_design)
button_close_brackets = Button(root, text=')', command=close_bracket, **regular_button_design)
button_open_brackets.grid(row=1, column=0)
button_close_brackets.grid(row=1, column=1)

button_clear = Button(root, text='CE', command=clear, **regular_button_design)
button_clear.grid(row=1, column=3)

button_convert_percentage = Button(root, text='%', command=lambda: button_operation('%'), **regular_button_design)
button_convert_percentage.grid(row=1, column=2)


# Create and position numbers 0 - 9
numbers = [Button(root, text=i, command=get_number(i), **regular_button_design) for i in range(1, 10)]

for index, number_button in enumerate(numbers[::-1]):
    column = 2 - (index % 3)
    row = (index // 3) + 2
    number_button.grid(row=row, column=column)
numbers.insert(0, Button(root, text='0', **regular_button_design, command=lambda: button_click(0)))
numbers[0].grid(row=5, column=0)



# Create buttons for = and . (Row 5)
button_equals = Button(root, text='=', **regular_button_design, command=button_equal)
button_equals.grid(row=5, column=2,)

button_floating_point = Button(root, text='.', command=lambda: button_click('.'), **regular_button_design)
button_floating_point.grid(row=5, column=1)


# Create + - * / (Column 3)
button_add = Button(root, text='+', command=lambda: button_operation('+'), **regular_button_design)
button_subtract = Button(root, text='-', command=lambda: button_operation('-'), **regular_button_design)
button_multiply = Button(root, text='*', command=lambda: button_operation('*'), **regular_button_design)
button_divide = Button(root, text='/', command=lambda: button_operation('/'), **regular_button_design)
button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)


root.mainloop()
