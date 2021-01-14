#!/usr/bin/python

"""
Install instructions:
- check tkinter installation: 
    :$ python3 -m tkinter
    if needed apt-get install python-tk 
"""

import tkinter as tk
submit = None
entry = None


def submit_str():
    pass


if __name__ == "__main__":
    top = tk.Tk()
    
    label = tk.Text(top, text="Hello").grid(0, 0)
    submit = tk.Button(top, text="World", command = submit_str).grid(1, 1)
    entry = tk.Entry(top).grid(1, 0)
    
    # add widgets
    
    
    top.mainloop()
