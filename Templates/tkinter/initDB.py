from random import randint, shuffle


NAMES = ["Алексей", "Игорь", "Валерий", "Дмитрий", "Павел"]
LNAMES = ["Иванов", "", "", "", ""]
MNAMES = ["Игоревич", "Олегович", "Максимович", "Иванович", "Всеволодвич", "Константинович"]
CITIES = ["Москва", "Курск", "Тверь"]


def main():
    f = open("data.txt", 'w')
    shuffle(NAMES)
    shuffle(LNAMES)
    for name in NAMES:
        for last in LNAMES:
            f.write("--\n")
            f.write("first_name={}\n".format(name))
            f.write("middle_name={}\n".format(last))
            middle = MNAMES[randint(0, len(MNAMES)-1)]
            f.write("middle_name={}\n".format(middle))
            f.write("document={Passport}\n")
            serial = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
            f.write("serial={}\n".format(serial))
            number = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
            number += str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
            f.write("number={}\n".format(number))
            birth = "04.05.93"
            f.write("birth_date={}".format(birth))
            location = CITIES[randint(0, len(CITIES)-1)]
            f.write("birth_location={}\n".format(location))
    f.close()


if __name__ == "__main__":
    main()
