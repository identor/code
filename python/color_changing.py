from tkinter import *

class Widget:
    def __init__(self):
        window = Tk()
        window.title("Changed Label Demo")

        self.__label = Label(window, text="Programming is fun")

        self.__color = IntVar()
        rb_default = Radiobutton(window, text="Default")
        rb_default["variable"] = self.__color
        rb_default["value"] = 0
        rb_default["command"] = self.label_handler
        rb_red = Radiobutton(window, text="Red", bg="RED")
        rb_red["variable"] = self.__color
        rb_red["value"] = 1
        rb_red["command"] = self.label_handler
        rb_yellow = Radiobutton(window, text="Yellow", bg="YELLOW")
        rb_yellow["variable"] = self.__color
        rb_yellow["value"] = 2
        rb_yellow["command"] = self.label_handler

        self.__label.grid(row=1, column=1)
        rb_default.grid(row=1, column=2)
        rb_red.grid(row=1, column=3)
        rb_yellow.grid(row=1, column=4)
        

        window.mainloop()

    def label_handler(self):
        if self.__color.get() == 1:
            self.__label["fg"] = "RED"
        elif self.__color.get() == 2:
            self.__label["fg"] = "YELLOW"
        else:
            self.__label["fg"] = "BLACK"
                
Widget()
