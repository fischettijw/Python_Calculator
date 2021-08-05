from tkinter import *
import os
os.system('cls')


def emptyfunc():
    # Code to be written
    pass


root = Tk()

# Main Menu
mainmenu = Menu(root)

# Menu 1
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Open", command=emptyfunc)
filemenu.add_command(label="Save", command=emptyfunc)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

# Menu 2
toolmenu = Menu(mainmenu, tearoff=0)
toolmenu.add_command(label="Find", command=emptyfunc)
toolmenu.add_command(label="Debugger", command=emptyfunc)
toolmenu.add_command(label="Replace", command=emptyfunc)

# Menu 3
helpmenu = Menu(mainmenu, tearoff=True)
helpmenu.add_command(label="Documentation", command=emptyfunc)


mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="Tools", menu=toolmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)


root.config(menu=mainmenu)
root.mainloop()
