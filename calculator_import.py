import tkinter as tk
import keyboard
from math import *
import os
os.system('cls')

global txt_display, btn_eval


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
