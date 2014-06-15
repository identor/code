from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Frame

class Login:
    def __init__(self):
        root = Tk()
        self.frm_top = Frame(root, bg='#00AAAA', width=200, height=50)
        self.frm_bot = Frame(root, bg='#AAAA00', width=200, height=50)
        self.frm_left = Frame(root, bg='#AA0000', width=50, height=200)
        self.frm_right = Frame(root, bg='#0000AA', width=200, height=50)
        self.frm_center = Frame(root, bg='#AAAAAA', width=200, height=200)
        self.frm_top.pack(fill='x')
        self.frm_center.pack(fill='both')
        self.frm_bot.pack(fill='x')
        self.frm_left.pack(sticky='W', fill='y')
        
