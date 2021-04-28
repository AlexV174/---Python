# Task 1

var = ['разработка', 'сокет', 'декоратор']
 
for line in var:
    print('type: {}'.format(type(line)))
    print('content: {}'.format(line))

var = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
       b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
       b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

for line in var:
    print('type: {}'.format(type(line)))
    print('content: {}'.format(line))

print("*"*100)
# Task 2

var = [b'class', b'function', b'method']

for line in var:
    print('type: {}'.format(type(line)))
    print('content: {}'.format(line))

print("*"*100)

# Task 3

var1 = b'attribute'
#var2 = b'класс'
#var3 = b'функция'
var4 = b'type'
# Var2 and Var3

# Task 4

main = ['разработка', 'администрирование', 'protocol', 'standard']
for i in main:
    a = i.encode('UTF-8')
    print(a, type(a))
    b = bytes.decode(a, 'UTF-8')
    print(b, type(b))

# Task 5

import subprocess

ping = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_now in ping:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i < 10:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            break
