from tkinter import END

from pandas import array

def clear(display_to_clear, *lists_to_clear):
    display_to_clear.delete(0, END)
    for lst in lists_to_clear:
        lst.clear()

def append_and_display(item_to_add, array_to_display, item_to_display_to):
    array_to_display.append(item_to_add)
    print('Display', array_to_display)
    item_to_display_to.delete(0, END)
    item_to_display_to.insert(0, ''.join(array_to_display))


evaluation_expression = []
expression_to_display = []

def button_clicked(item_selected, display, evaluation_expression=evaluation_expression, expression_to_display=expression_to_display):
    alternate_displays = {'²': '**2', '√': '**0.5', '%': '/100'}
    if item_selected not in alternate_displays.keys() and item_selected not in ['=', 'CE']:
        evaluation_expression.append(item_selected)
        append_and_display(item_selected, expression_to_display, display)
    elif item_selected in alternate_displays.keys():
        evaluation_expression.append(alternate_displays[item_selected])
        append_and_display(item_selected, expression_to_display, display)
    elif item_selected == '=':
        total = str(eval(''.join(evaluation_expression)))
        clear(display, evaluation_expression, expression_to_display)
        evaluation_expression.append(total)
        append_and_display(total, expression_to_display, display)
    elif item_selected == 'CE':
        clear(display, evaluation_expression, expression_to_display)

