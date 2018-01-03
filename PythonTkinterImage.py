# PythonTkinter.py

# Taken from https://www.python-course.eu/tkinter_labels.php

# C:\Python27\python.exe -i "$(FULL_CURRENT_PATH)"

from Tkinter import *
import os

root = Tk()
# It will only display a .gif image
# logo = PhotoImage(file="C:\\Users\\casey\\Desktop\\Desktop\\Photos\\iPhone\\Iphone Files 10-7\\118APPLE\\IMG_8011.gif")
# logo = PhotoImage(file='C:'+os.sep+'Desktop'+os.sep+'Photos'+os.sep+'Devices'+os.sep+'iPhone'+os.sep+'All Photos- Timestamped'+os.sep+'2014-11-01 214144.jpg')
logo = PhotoImage(file='C:'+os.sep+'Projects'+os.sep+'Tutorials'+os.sep+'Tkinter'+os.sep+'Python-Course'+os.sep+'cartoon_butterfly_flaying_colour_animation_clipart.gif')

w1 = Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation).pack(side="left")
root.mainloop()