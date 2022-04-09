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