# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv()

import csv
import re
import chardet


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
            content = content.decode(chardet.detect(content)['encoding'])
            os_prod_list = file, re.findall('Изготовитель системы:\s+(\w+)', content)[0].strip()
            os_name_list = file, re.findall('Название ОС:\s+([\w\.\s]+)\n', content)[0].strip()
            os_code_list = file, re.findall('Код продукта:\s+([\w\-]+\w+)', content)[0].strip()
            os_type_list = file, re.findall('Тип системы:\s+([\w\-\w\s\w]+)', content)[0].strip()

            main_data.extend([[os_prod_list[1], os_name_list[1], os_code_list[1], os_type_list[1]]])

    return main_data


def write_to_csv(csv_file):
    to_write = get_data()
    with open(csv_file, 'w', encoding='utf-8', newline="") as main_data_file:
        md_writer = csv.writer(main_data_file, quoting=csv.QUOTE_ALL, quotechar="\"")
        md_writer.writerow(to_write[0])
        md_writer.writerows(to_write[1:], )
    return print(f'Данные находятся в: {csv_file}')
