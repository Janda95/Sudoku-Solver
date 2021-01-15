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

class Application(tk.Frame):
    
    def __init__(self, hangman, master):
        super().__init__(master)
        self.master = master
        self.hangman = hangman
        self.pack()
        self.create_widgets()
        
        
    def create_widgets(self):
        # Hello button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        # Submit button
        self.submit = tk.Button(self)
        self.submit["text"] = "Submit"
        self.submit["command"]
        
        # Quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


    def say_hi(self):
        print("hi there, everyone!")     
        
   
    def submit_guess(self):
        msg = "Submit: " + ""
        print(msg)


if __name__ == "__main__":
    '''top = tk.Tk()
    
    label = tk.Text(top, text="Hello").grid(0, 0)
    submit = tk.Button(top, text="World", command = submit_str).grid(1, 1)
    entry = tk.Entry(top).grid(1, 0)
    
    # add widgets
    top.mainloop()
    '''
    
    root = tk.Tk()
    hangman = None
    app = Application(root, hangman, root)
    
    app.mainloop()
