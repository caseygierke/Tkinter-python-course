# PythonTkinter.py

# Taken from https://www.python-course.eu/tkinter_labels.php

# C:\Python27\python.exe -i "$(FULL_CURRENT_PATH)"

from Tkinter import *
# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *

root = Tk()


w = Label(root, text="Hello Tkinter!")
w.pack()

root.mainloop()