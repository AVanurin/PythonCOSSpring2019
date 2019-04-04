from tkinter import Frame, Label


class InformationFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def remake(self, data):

        temp = "Фамилия:{}".format(data["last_name"])
        ln_label = Label(self, text=temp).pack(side="top", anchor='w')

        temp = "Имя:{}".format(data["first_name"])
        fn_label = Label(self, text=temp).pack(side="top", anchor='w')

        temp = "Отчество:{}".format(data["middle_name"])
        mn_label = Label(self, text=temp).pack(side="top", anchor='w')

        document = data["document"]

        if document["type"] == "Passport":
            temp = "Тип документа: Пасспорт РФ"
            type_label = Label(self, text=temp).pack(side="top", anchor='w')

            temp = "Номер документа:{}-{}".format(document["serial"], document["number"])
            dnumber_label = Label(self, text=temp).pack(side="top", anchor='w')

        temp = "Дата рождения:{}".format(data["birth_date"])
        dbirth_label = Label(self, text=temp).pack(side="top", anchor='w')

        temp = "Место рождения:{}".format(data["birth_location"])
        lbirth_label = Label(self, text=temp).pack(side="top", anchor='w')
