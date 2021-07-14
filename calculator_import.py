import tkinter as tk

global txt_display


def btn_click(num):
    txt_display.delete(0, tk.END)
    txt_display.insert(0, num)
