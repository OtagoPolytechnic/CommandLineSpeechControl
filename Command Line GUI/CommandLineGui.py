from tkinter import *
from tkinter import ttk

import speech_recognition as sr
import os

root = Tk()

root.wm_title("Command Line GUI")
root.resizable(width = False, height = False)

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True)
frameOne = ttk.Frame(panedwindow, width = 100, height = 300, relief = SOLID)
frameTwo = ttk.Frame(panedwindow, width = 400, height = 400, relief = SOLID)
panedwindow.add(frameOne, weight = 1)
panedwindow.add(frameTwo, weight = 4)

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

treeview = ttk.Treeview(frameOne, height = 20)
treeview.pack()
treeview.insert('', '0', 'item1', text = 'Instructions')
treeview.insert('item1', 'end', 'Intrsuctions', text = 'Instructions')
treeview.insert('', '1', 'item2', text = 'Linux Commands')
treeview.insert('item2', 'end', 'BasicCommands', text = 'Basic Commands')
treeview.insert('item2', 'end', 'IntermediateCommands', text = 'Intermediate Commands')
treeview.insert('item2', 'end', 'AdvancedCommands', text = 'Advanced Commands')
treeview.insert('', '2', 'item3', text = 'Shortcuts/Hotkeys')
treeview.insert('item3', 'end', 'Shortcuts', text = 'Keyboard Shortcuts')

API = StringVar()

ttk.Radiobutton(frameTwo, text = 'Python', variable = API, value = 'Python').pack(side = LEFT, padx = 5)
ttk.Radiobutton(frameTwo, text = 'Google', variable = API, value = 'Google').pack(side = LEFT, padx = 5)
ttk.Radiobutton(frameTwo, text = 'Sphinx', variable = API, value = 'Sphinx').pack(side = LEFT, padx = 5)
ttk.Radiobutton(frameTwo, text = 'Local', variable = API, value = 'Local').pack(side = LEFT ,padx = 5)
ttk.Radiobutton(frameTwo, text = 'Other', variable = API, value = 'Other').pack(side = LEFT, padx = 5)

button1 = ttk.Button(bottomframe, text = "Pause").pack(side = LEFT, padx = 5, pady = 5)
button2 = ttk.Button(bottomframe, text = "Play").pack(side = LEFT, padx = 5, pady = 5)
button3 = ttk.Button(bottomframe, text = "Stop").pack(side = LEFT, padx = 5, pady = 5)

root.mainloop()

