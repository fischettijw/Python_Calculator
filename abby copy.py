# region imports
import tkinter as tk
import os

os.system("cls")

# endregion imports

# region Variables
clear_display = True
# endregion Variables

# region Functions


def btn_click_number(num):
    global clear_display
    if clear_display == True:
        btn_click_clear()
    current = txt_display.get()
    txt_display.delete(0, tk.END)
    txt_display.insert(0, str(current) + str(num))
    clear_display = False


def btn_click_oper(oper):
    global clear_display
    if ck_box_status.get() == True:
        btn_click_equal()  # MODIFICATION
    current = txt_display.get()
    txt_display.delete(0, tk.END)
    txt_display.insert(0, str(current) + str(oper))
    clear_display = False


def btn_click_clear():
    txt_display.delete(0, tk.END)


def btn_click_equal():
    global clear_display
    current = txt_display.get()
    btn_click_clear()
    txt_display.insert(0, str(eval(current)))
    clear_display = True


# endregion Functions
# region Window
win = tk.Tk()
win.geometry("+100+100")
win.title("Abigail's Simple Calculator")
win.option_add("*Entry*font", 'courier 16 bold')
win.option_add("*Button*font", 'courier 18 bold')
win.option_add("*Button*background", 'gray90')

# endregion Window

# region GUI define widgets
ck_box_status = tk.BooleanVar(win)
ck_box = tk.Checkbutton(win,
                        variable=ck_box_status,
                        onvalue=True, offvalue=False)
txt_display = tk.Entry(win,
                       borderwidth=5,
                       justify="right")

btn_7 = tk.Button(win,
                  text="7",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(7))
btn_8 = tk.Button(win,
                  text="8",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(8))
btn_9 = tk.Button(win,
                  text="9",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(9))
btn_oper_plus = tk.Button(win,
                          text="+",
                          width=5,
                          pady=20,
                          justify="center",
                          relief=tk.GROOVE,
                          command=lambda: btn_click_oper('+'))

btn_4 = tk.Button(win,
                  text="4",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(4))
btn_5 = tk.Button(win,
                  text="5",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(5))
btn_6 = tk.Button(win,
                  text="6",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(6))
btn_oper_minus = tk.Button(win,
                           text="-",
                           width=5,
                           pady=20,
                           justify="center",
                           relief=tk.GROOVE,
                           command=lambda: btn_click_oper('-'))
btn_1 = tk.Button(win,
                  text="1",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(1))
btn_2 = tk.Button(win,
                  text="2",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(2))
btn_3 = tk.Button(win,
                  text="3",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(3))
btn_oper_multiply = tk.Button(win,
                              text="x",
                              width=5,
                              pady=20,
                              justify="center",
                              relief=tk.GROOVE,
                              command=lambda: btn_click_oper('*'))

btn_0 = tk.Button(win,
                  text="0",
                  width=5,
                  pady=20,
                  justify="center",
                  relief=tk.GROOVE,
                  command=lambda: btn_click_number(0))
btn_clr = tk.Button(win,
                    text="clr",
                    width=5,
                    pady=20,
                    justify="center",
                    relief=tk.GROOVE,
                    command=btn_click_clear)
btn_equal = tk.Button(win,
                      text="=",
                      width=5,
                      pady=20,
                      justify="center",
                      relief=tk.GROOVE,
                      command=btn_click_equal)
btn_oper_divide = tk.Button(win,
                            text="÷",
                            width=5,
                            pady=20,
                            justify="center",
                            relief=tk.GROOVE,
                            command=lambda: btn_click_oper('/'))
# endregion GUI define widgets

# region GUI place widgets on screen

ck_box.grid(row=0, column=0)
txt_display.grid(row=0,
                 column=1,
                 columnspan=3,
                 padx=10,
                 pady=(10, 20),
                 sticky=tk.EW)

btn_7.grid(row=1, column=0, padx=(10, 0), pady=(0, 10))
btn_8.grid(row=1, column=1, padx=(10, 0), pady=(0, 10))
btn_9.grid(row=1, column=2, padx=(10, 0), pady=(0, 10))
btn_oper_plus.grid(row=1, column=3, padx=(10, 10), pady=(0, 10))

btn_4.grid(row=2, column=0, padx=(10, 0), pady=(0, 10))
btn_5.grid(row=2, column=1, padx=(10, 0), pady=(0, 10))
btn_6.grid(row=2, column=2, padx=(10, 0), pady=(0, 10))
btn_oper_minus.grid(row=2, column=3, padx=(10, 10), pady=(0, 10))

btn_1.grid(row=3, column=0, padx=(10, 0), pady=(0, 10))
btn_2.grid(row=3, column=1, padx=(10, 0), pady=(0, 10))
btn_3.grid(row=3, column=2, padx=(10, 0), pady=(0, 10))
btn_oper_multiply.grid(row=3, column=3, padx=(10, 10), pady=(0, 10))

btn_0.grid(row=4, column=0, padx=(10, 0), pady=(0, 10))
btn_clr.grid(row=4, column=1, padx=(10, 0), pady=(0, 10))
btn_equal.grid(row=4, column=2, padx=(10, 0), pady=(0, 10))
btn_oper_divide.grid(row=4, column=3, padx=(10, 10), pady=(0, 10))
# endregion GUI place widgets on screen

win.mainloop()
