from tkinter import *

class Widget:    
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")

        self.__canvas = Canvas(window, width=200, height=100, bg="white")
        self.__canvas.pack()

        btnframe = Frame(window)
        btnframe.pack()

        draw_rectangle = Button(btnframe, text="Rectangle",
            command=self.drawRect)
        draw_oval = Button(btnframe, text="Oval",
            command=self.drawOval)

        draw_arc = Button(btnframe, text="Arc",
            command=self.drawArc)

        draw_string = Button(btnframe, text="String",
            command=self.drawString)

        clear = Button(btnframe, text="Clear",
            command=self.clear)

        draw_rectangle.grid(row=1, column=1)
        draw_oval.grid(row=1, column=2)
        draw_arc.grid(row=1, column=3)
        draw_string.grid(row=1, column=4)
        clear.grid(row=1, column=5)
        
        window.mainloop()

    def drawRect(self):
        self.__canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def drawOval(self):
        self.__canvas.create_oval(10, 10, 190, 90, fill="red",
            tags="oval")
    def drawArc(self):
        self.__canvas.create_arc(10, 10, 190, 90, start=0,
            extent=90, width=8, fill="red", tag ="arc")

    def drawString(self):
        self.__canvas.create_text(60, 40, text ="Hi, I am a string",
            font="Times 10 bold underline", tags="string")

    def clear(self):
        self.__canvas.delete("rect", "oval", "arc", "string")

Widget()
