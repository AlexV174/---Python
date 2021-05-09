from socket import SOCK_STREAM, socket
import base64
from setting import *
import sys

if '-a' in sys.argv:
    addr = str(sys.argv[2])
    port = int(sys.argv[4])
else:
    addr = '192.168.0.2'
    port = int(sys.argv[2])

sock = socket(type=SOCK_STREAM)
sock.bind((addr, port))
sock.listen(1)
conn, addr = sock.accept()

print(f'Connection with {addr} complete')

while True:
    data = conn.recv(1024)
    data_decode = eval(base64.b64decode(data))
    message_answer = data_decode['message']
    message_time_answer = data_decode['time']
    message_account_name = data_decode['user']['account_name']

    if message_answer == 'close':
        data_answer = f'You close connection' \
                      f' {message_account_name}.'.encode(CODE)
        conn.send(data_answer.upper())
        break
    else:
        data_answer = f'Your message: {message_answer} в' \
                      f' {message_time_answer}'.encode(CODE)
        conn.send(data_answer.upper())

print(f'Connection with {addr} ends')
conn.close()
