from tkinter import *

class UIOne:
    def __init__(self):
        window = Tk()
        window.title("UI One")
        
        label = Label(window, text="Hello World")
        button = Button(window, text="OK", command=self.ok_clicked)
        label.pack()
        button.pack()
        
    def ok_clicked(self):
        print("ok clicked")
        
class UITwo:
    def __init__(self):
        window = Tk()
        window.title("UI Two")
