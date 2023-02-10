def data_collector():
    nsurname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите описание телефона: ')
    print()
    data = [nsurname, name, phone, comment]
    return data

def model_record(data):
    file = 'form1_file.txt'
    with open(file, 'a', encoding="utf-8") as data1:
        data1.write(f'Фамилия: {data[0]}, \nИмя: {data[1]}, \nНомер телефона: {data[2]}, \nОписание: {data[3]}\n\n')
        
    file = 'form2_file.txt'
    with open(file, 'a', encoding="utf-8") as data2:
        data2.write(f'Фамилия: {data[0]}, Имя: {data[1]}, Номер телефона: {data[2]}, Описание: {data[3]}\n')

def model_print():
    with open('form2_file.txt', 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end = '')