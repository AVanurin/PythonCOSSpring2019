from tkinter import Frame
from tkinter import Entry, Button


class SearchFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        text_field = Entry(self)
        text_field.pack(side="top", fill='x')

        button = Button(self, text="Поиск", command=self.callback)
        button.pack(side="top", fill='x')

        self.listener = None

    def callback(self):
        if self.listener:
            self.listener()

    def set_button_listener(self, f):
        self.listener = f
