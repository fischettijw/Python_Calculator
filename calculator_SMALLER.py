# region Links

# https://www.youtube.com/watch?v=F5PfbC5ld-Q
# https://www.youtube.com/watch?v=XhCfsuMyhXo
# https://www.youtube.com/watch?v=oq3lJdhnPp8

'''
Use tkinter and Python in the browser with Repl.it
https://replit.com/

https://www.youtube.com/watch?v=2BeyOrUKRD4
'''

# endregion Links

# region Imports
import tkinter as tk
import time
import keyboard
from math import *
# from calculator_import import *
import os
os.system('cls')

# endregion Imports

# region Constants
undo = []
clear_display = True
padx0505 = (5, 5)
padx0500 = (5, 0)
pady15 = 15
pady0005 = (0, 5)
pady0510 = (5, 10)

# endregion Constants

# region functions


def btn_click_number(num):
    global clear_display
    if clear_display:
        txt_display.delete(0, tk.END)
        clear_display = False
    current = txt_display.get()
    txt_display.delete(0, tk.END)
    txt_display.insert(0, str(current)+str(num))


def btn_click_oper(oper):
    global clear_display
    current = txt_display.get()
    txt_display.delete(0, tk.END)
    txt_display.insert(0, str(current)+str(oper))
    clear_display = False


def btn_click_equal():
    btn_eval(None)


def btn_eval(event):
    global clear_display
    undo.append(txt_display.get())
    current = txt_display.get()
    txt_display.delete(0, tk.END)
    try:
        txt_display.insert(0, str(eval(current)))
    except ZeroDivisionError as e:
        txt_display.insert(0, 'Divide By Zero')
        win.after(1000, btn_click_clear)
    except:
        txt_display.insert(0, 'Invalid Syntax')
        win.after(1000, btn_click_clear)
    clear_display = True


def btn_click_clear():
    txt_display.delete(0, tk.END)
    clear_display = False


def undo_expression(event):
    txt_display.delete(0, tk.END)
    if len(undo) > 0:
        txt_display.insert(0, str(undo.pop()))
    else:
        txt_display.insert(0, 'No Previous Expression')
        win.after(1000, btn_click_clear)


# endregion functions
# region root Tkinter window
win = tk.Tk()
win.geometry('+15+15')
win.title('Simple Calculator by Abigail Lightle')
win.option_add("*Entry*font", 'courier 16 bold')
win.option_add("*Button*font", 'courier 18 bold')
win.option_add("*Button*background", 'gray90')

# endregion root Tkinter window

# region GUI Define widgets
txt_display = tk.Entry(win,  borderwidth=5, justify="right")

btn_1 = tk.Button(win, text="1", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(1))
btn_2 = tk.Button(win, text="2", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(2))
btn_3 = tk.Button(win, text="3", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(3))
btn_4 = tk.Button(win, text="4", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(4))
btn_5 = tk.Button(win, text="5", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(5))
btn_6 = tk.Button(win, text="6", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(6))
btn_7 = tk.Button(win, text="7", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(7))
btn_8 = tk.Button(win, text="8", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(8))
btn_9 = tk.Button(win, text="9", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(9))
btn_0 = tk.Button(win, text="0", width=5, pady=pady15,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(0))
btn_oper_plus = tk.Button(win, text="+", width=5, pady=pady15,
                          justify="center", relief=tk.GROOVE, command=lambda: btn_click_oper('+'))
btn_oper_minus = tk.Button(win, text="-", width=5, pady=pady15,
                           justify="center", relief=tk.GROOVE, command=lambda: btn_click_oper('-'))
btn_oper_multiply = tk.Button(win, text="*", width=5, pady=pady15,
                              justify="center", relief=tk.GROOVE, command=lambda: btn_click_oper('*'))
btn_oper_divide = tk.Button(win, text="/", width=5, pady=pady15,
                            justify="center", relief=tk.GROOVE, command=lambda: btn_click_oper('/'))
btn_clear = tk.Button(win, text="clr", width=5, pady=pady15,
                      justify="center", relief=tk.GROOVE, command=btn_click_clear)

btn_equal = tk.Button(win, text="=", width=5, pady=pady15,
                      justify="center", relief=tk.GROOVE, command=btn_click_equal)
# endregion GUI Define widgets

# region GUI Grid
btn_1.grid(row=3, column=0, padx=padx0500, pady=pady0005)
btn_2.grid(row=3, column=1, padx=padx0500, pady=pady0005)
btn_3.grid(row=3, column=2, padx=padx0505, pady=pady0005)
btn_oper_multiply.grid(row=3, column=3, padx=padx0505, pady=pady0005)

btn_4.grid(row=2, column=0, padx=padx0500, pady=pady0005)
btn_5.grid(row=2, column=1, padx=padx0500, pady=pady0005)
btn_6.grid(row=2, column=2, padx=padx0505, pady=pady0005)
btn_oper_minus.grid(row=2, column=3, padx=padx0505, pady=pady0005)

btn_7.grid(row=1, column=0, padx=padx0500, pady=pady0005)
btn_8.grid(row=1, column=1, padx=padx0500, pady=pady0005)
btn_9.grid(row=1, column=2, padx=padx0505, pady=pady0005)
btn_oper_plus.grid(row=1, column=3, padx=padx0505, pady=pady0005)

btn_0.grid(row=4, column=0, padx=padx0505, pady=pady0005)
btn_equal.grid(row=4, column=2, padx=padx0505, pady=pady0005)

btn_oper_divide.grid(row=4, column=3, padx=padx0505, pady=pady0005)
btn_clear.grid(row=4, column=1, padx=padx0505, pady=pady0005)

txt_display.grid(row=0, column=0, columnspan=4,
                 padx=padx0500, pady=pady0510, sticky=tk.EW)
# endregion Grid

# region GUI Events
txt_display.bind('<Return>', btn_eval)
win.bind('<Control-KeyPress-z>', undo_expression)
# win.bind('<Control-d>', txt_display.delete(0, tk.END))

# endregion Evenst

# region GUI misc
txt_display.focus_set()

# endregion GUI misc

win.mainloop()
