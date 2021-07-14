# https://www.youtube.com/watch?v=F5PfbC5ld-Q
# https://www.youtube.com/watch?v=XhCfsuMyhXo
# https://www.youtube.com/watch?v=oq3lJdhnPp8

# region Imports
import tkinter as tk
import keyboard
from math import *
# from calculator_import import *
import os
os.system('cls')

# endregion Imports


# region functions


def btn_click_number(num):
    current = txt_display.get()
    txt_display.delete(0, tk.END)
    txt_display.insert(0, str(current)+str(num))


def btn_click_oper(oper):
    current = txt_display.get()
    txt_display.delete(0, tk.END)
    txt_display.insert(0, str(current)+str(oper))


def btn_click_equal():
    btn_eval(None)


def btn_eval(event):
    if keyboard.is_pressed('ctrl') or event == None:
        # if keyboard.is_pressed('ctrl+shift+alt'):
        current = txt_display.get()
        txt_display.delete(0, tk.END)
        txt_display.insert(0, str(eval(current)))
# endregion functions


# region root Tkinter window
win = tk.Tk()
win.geometry('+200+10')
win.title('Simple Calculator')
win.option_add("*Entry*font", 'courier 36 bold')
win.option_add("*Button*font", 'courier 48 bold')
win.option_add("*Button*background", 'gray90')

# endregion root Tkinter window


# region GUI Define widgets
txt_display = tk.Entry(win,  borderwidth=5, justify="right")

btn_1 = tk.Button(win, text="1", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(1))
btn_2 = tk.Button(win, text="2", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(2))
btn_3 = tk.Button(win, text="3", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(3))
btn_4 = tk.Button(win, text="4", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(4))
btn_5 = tk.Button(win, text="5", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(5))
btn_6 = tk.Button(win, text="6", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(6))
btn_7 = tk.Button(win, text="7", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(7))
btn_8 = tk.Button(win, text="8", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(8))
btn_9 = tk.Button(win, text="9", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(9))
btn_0 = tk.Button(win, text="0", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number(0))
btn_oper = tk.Button(win, text="+", width=5, pady=20,
                     justify="center", relief=tk.GROOVE, command=lambda: btn_click_oper('+'))
btn_equal = tk.Button(win, text="=", width=5, pady=20,
                      justify="center", relief=tk.GROOVE, command=btn_click_equal)
# endregion GUI Define widgets


# region GUI Grid
btn_1.grid(row=3, column=0, padx=(10, 0), pady=(0, 10))
btn_2.grid(row=3, column=1, padx=(10, 0), pady=(0, 10))
btn_3.grid(row=3, column=2, padx=(10, 10), pady=(0, 10))

btn_4.grid(row=2, column=0, padx=(10, 0), pady=(0, 10))
btn_5.grid(row=2, column=1, padx=(10, 0), pady=(0, 10))
btn_6.grid(row=2, column=2, padx=(10, 10), pady=(0, 10))

btn_7.grid(row=1, column=0, padx=(10, 0), pady=(0, 10))
btn_8.grid(row=1, column=1, padx=(10, 0), pady=(0, 10))
btn_9.grid(row=1, column=2, padx=(10, 10), pady=(0, 10))

btn_0.grid(row=4, column=0, padx=(10, 10), pady=(0, 10))
btn_oper.grid(row=4, column=1, padx=(10, 10), pady=(0, 10))
btn_equal.grid(row=4, column=2, padx=(10, 10), pady=(0, 10))

txt_display.grid(row=0, column=0, columnspan=3,
                 padx=10, pady=(10, 20), sticky=tk.EW)
# endregion Grid


# region GUI Events
txt_display.bind('<Return>', btn_eval)

# endregion Evenst


# region GUI misc
txt_display.focus_set()

# endregion GUI misc

win.mainloop()
