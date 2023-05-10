import csv
fileCVS = "data.csv"

target_string = "Ім\'я', 'Прізвище', 'Вік','Телефон"

def check_string(file_name, target_string):
    with open(file_name, "r", encoding="utf8") as file:
        file_contents = file.read()
        if target_string not in file_contents:
            with open(file_name, 'w', newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(['Ім\'я', 'Прізвище', 'Вік','Телефон'])

def userInput():
    name = input("Ім'я - ")
    pr = input("Прізвище - ")
    vik = (input("Вік - "))
    phone = (input("Номер телефону - "))
    return [name, pr, vik, phone]

def regim():
    while True:
        print("1 = Зберегти OR 2 = Показати")
        select = input("Hежим -> ")
        if select  == '1':
            with open(fileCVS, 'a', newline="", encoding="utf-8") as file:
                check_string(fileCVS, target_string)
                w = csv.writer(file)
                dataUser = userInput()
                w.writerow(dataUser)
            break
        elif select == '2':
            with open(fileCVS, 'r', encoding="utf-8") as file:
                reader = csv.reader(file)
                for i in reader:
                    print(*i)
            break
regim()
