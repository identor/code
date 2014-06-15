from tkinter import *

class Widget:
    def __init__(self):
        window = Tk()
        window.title("Widget Demo")

        frame1 = Frame(window)
        frame1.pack()
        
        self.v1 = IntVar()
        self.__cb_bold = Checkbutton(frame1, variable=self.v1, text="bold", 
                   command=self.cb_handle)
        
        self.v2 = IntVar()
        rb_red = Radiobutton(frame1, variable=self.v2, text="Red",
            bg="red", command=self.rb_handle, value=1)
        rb_yellow = Radiobutton(frame1, variable=self.v2, text="Yellow",
            bg="Yellow", command=self.rb_handle, value=2)

        self.__cb_bold.grid(row=1, column=1)
        rb_red.grid(row=1, column=2)
        rb_yellow.grid(row=1, column=3)

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")
        self.name = StringVar()
        entry = Entry(frame2, textvariable=self.name)
        getname = Button(frame2, text="Get Name",
                         command=self.name_handle)
        message = Message(frame2, text="It is a widget demo")
        
        label.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        getname.grid(row=1, column=3)
        message.grid(row=1, column=4)

        text = Text(window)
        text.pack()
        text.insert(END,
                    "Tip\nThe best way to learn tkinter is to read ")
        text.insert(END,
                    "these carefully designed examples and use them ")
        text.insert(END, "to create your own applications. ")

        window.mainloop()

    def cb_handle(self):
        print("check button is "
              + ("checked" if self.v1.get() == 1 else "unchecked"))
        self.__cb_bold["text"] = "BOLD" if self.v1.get() == 1 else "bold"

    def rb_handle(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + "is selected")

    def name_handle(self):
        print(("Your name is: " + self.name.get()))

Widget()
