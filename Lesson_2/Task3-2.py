# Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import os
import yaml


def write_to_yaml(filename, data):

    with open(os.path.join(os.getcwd(), filename), 'w',
              encoding='utf-8') as f_in:
        yaml.dump(data, f_in, default_flow_style=False, allow_unicode=True)

    with open(os.path.join(os.getcwd(), filename), 'r',
              encoding='utf-8') as f_out:
        data_out = yaml.load(f_out, Loader=yaml.SafeLoader)

    if data == data_out:
        print('Данные совпадают.')
    else:
        print('Данные не совпадают!')



data = {
    'items': ['Nvidia', 'AMD'],
    'quantity': 12,
    'prices': {
        'Nvidia': '1000 €',
        'AMD': '800 €'
    }
}
write_to_yaml('file.yaml', data)