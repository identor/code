from tkinter import *

class MyWindow:

    def __init__(self):
        self.__window = Tk()
        self.__button = Button(self.__window, text="Click!", command=self.message)
        self.__button.pack()
        self.__window.mainloop()

    def message(self):
        print("Hello!!")

def main():
    window = MyWindow()

main()
