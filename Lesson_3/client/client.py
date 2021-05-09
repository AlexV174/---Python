from socket import SOCK_STREAM, socket
from setting import *
import base64
import sys

if sys.argv:
    addr = str(sys.argv[2])
    port = int(sys.argv[4])

sock = socket(type=SOCK_STREAM)
sock.connect((addr, port))
print(f'{ACCOUNT_NAME} you enter at {TIME}')

while True:
    message_account = input('Print your message:')
    time_now = datetime.datetime.now()
    TIME = str(time_now.strftime("%d-%m-%Y %H:%M %S"))
    jim_msg = {
        'action': ACTION,
        'time': TIME,
        'type': TYPE,
        'user': {
            'account_name': ACCOUNT_NAME,
            'status': STATUS,
        },
        'encoding': CODE,
        'message': message_account,
    }
    jim_msg_encode = str(jim_msg).encode(CODE)
    jim_msg_encode_64 = base64.b64encode(jim_msg_encode)
    sock.send(jim_msg_encode_64)
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    if message_account == 'close':
        time_now = datetime.datetime.now()
        TIME = str(time_now.strftime("%d-%m-%Y %H:%M %S"))
        jim_msg = {
            'action': ACTION,
            'time': TIME,
            'type': TYPE,
            'user': {
                'account_name': ACCOUNT_NAME,
                'status': STATUS,
            },
            'encoding': CODE,
            'message': message_account
            }
        jim_msg_encode = str(jim_msg).encode(CODE)
        jim_msg_encode_64 = base64.b64encode(jim_msg_encode)
        sock.send(jim_msg_encode_64)
        data = sock.recv(1024)
        print(data.decode(CODE))
        break

print('You are disconnected')
sock.close()
