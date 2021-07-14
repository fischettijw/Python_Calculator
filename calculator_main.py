# https://www.youtube.com/watch?v=F5PfbC5ld-Q
# https://www.youtube.com/watch?v=XhCfsuMyhXo
# https://www.youtube.com/watch?v=oq3lJdhnPp8

import tkinter as tk
import keyboard
from math import *
# from calculator_import import *
import os
os.system('cls')

win = tk.Tk()
win.title('Simple Calculator')
win.option_add("*Entry*font", 'courier 36 bold')
win.option_add("*Button*font", 'courier 48 bold')
win.option_add("*Button*background", 'gray90')


def btn_click_number(num):
    if str(num) != '+' and str(num) != '=':
        current = txt_display.get()
        txt_display.delete(0, tk.END)
        txt_display.insert(0, str(current)+str(num))
    if str(num) == "=":
        current = txt_display.get()
        txt_display.delete(0, tk.END)
        txt_display.insert(0, str(eval(current)))
    if str(num) == "+":
        current = txt_display.get()
        txt_display.delete(0, tk.END)
        txt_display.insert(0, str(current)+str(num))


def btn_eval(event):
    if keyboard.is_pressed('ctrl'):
        # if keyboard.is_pressed('ctrl+shift+alt'):
        current = txt_display.get()
        txt_display.delete(0, tk.END)
        txt_display.insert(0, str(eval(current)))


txt_display = tk.Entry(win,  borderwidth=5, justify="right")
txt_display.grid(row=0, column=0, columnspan=3,
                 padx=10, pady=(10, 20), sticky=tk.EW)
txt_display.bind('<Return>', btn_eval)
# txt_display.bind('<Double-Button-3>', btn_eval)
txt_display.focus_set()

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
btn_p = tk.Button(win, text="+", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number('+'))
btn_e = tk.Button(win, text="=", width=5, pady=20,
                  justify="center", relief=tk.GROOVE, command=lambda: btn_click_number('='))

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
btn_p.grid(row=4, column=1, padx=(10, 10), pady=(0, 10))
btn_e.grid(row=4, column=2, padx=(10, 10), pady=(0, 10))


win.mainloop()
