# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра

import os
import json

# папка с отдельными файлами заказов в формате csv #
found_folder = 'C:/orders'

# папка с общим файлом orders.json ,в который пишутся
# данные из отдельных файлов формата csv #
write_to_folder = 'C:/order'

def write_order_to_json():

    folder = os.scandir(found_folder)

    with open(os.path.join(write_to_folder, 'orders.json'),
              'r', encoding='utf-8') as f:
        data_json = json.load(f)

    for found_file in folder:
        with open(found_file, 'r', encoding='utf-8') as f_in:
            data = tuple(item for item in f_in.read().split(','))

            order = {
                "item": data[0],
                "quantity": data[1],
                "price": data[2],
                "buyer": data[3],
                "date": data[4],
            }

        with open(os.path.join(write_to_folder, 'orders.json'),
                  'w', encoding='utf-8') as f_out:
            data_json['orders'].append(order)
            json.dump(data_json, f_out, indent=4)


write_order_to_json()