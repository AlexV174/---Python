import locale

var = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file', 'w+') as n:
    for i in var:
        n.write(i + '\n')
    n.seek(0)

print(n)

file_coding = locale.getpreferredencoding()

with open('test_file', 'r', encoding=file_coding) as n:
    for i in n:
        print(i)
    n.seek(0)