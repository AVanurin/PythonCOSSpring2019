from tkinter import Tk, messagebox
from banker_ui.InformationFrame import InformationFrame
from banker_ui.SearchFrame import SearchFrame


FILENAME = "data.txt"
D = {"first_name": "Alexey",
     "middle_name": "Maksimovich",
     "last_name": "Vanurin",
     "document": {"type": "Passport", "serial": "1234", "number": "12345"},
     "birth_date": "10.04.2018",
     "birth_location": "Moscow",
     }


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("250x300")
        self.root.title("Поиск по базе")
        self.root.resizable(False, False)

        top_frame = SearchFrame(self.root)
        top_frame.pack(side="top")
        top_frame.set_button_listener(self.button_was_clicked)
        self.info_frame = None

    def make_info_panel(self, d=None):
        if self.info_frame:
            self.info_frame.pack_forget()
        if d:
            info_frame = InformationFrame(self.root)
            info_frame.pack(side="top", pady=10)
            info_frame.remake(d)

    def run(self):
        self.root.mainloop()

    def button_was_clicked(self):
        self.make_info_panel(D)
        self.on_error()

    def on_error(self):
        messagebox.showerror("Ошибка", "Информация о человеке отсутсвует")


    def _load(self):
        f = open(FILENAME, 'r')


def main():
    App().run()


if __name__ == "__main__":
    main()
