import json
import socket
import sys
import time
import datetime

from my_project.settings.utils import get_message, send_message
from my_project.settings.variables import (ACCOUNT_NAME, ACTION, DEFAULT_PORT,
                              ERROR, PRESENCE, RESPONSE, TIME, DEFAULT_IP_ADDRESS, USER)

def create_presence(accounte_name='Guest'):
	time_now = datetime.datetime.now()
	time = str(time_now.strftime("%d-%m-%Y %H:%M %S"))
	out = {
		ACTION: PRESENCE,
		TIME: time,
		USER: {
			ACCOUNT_NAME: accounte_name
		}
	}
	return out

def process_ans(message):
	if RESPONSE in message:
		if message[RESPONSE] == 200:
			return '200 : OK'
		return f'400 : {message[ERROR]}'
	raise ValueError

def main():
	
	try:
		if '-a' in sys.argv:
			server_address = sys.argv[sys.argv.index('-a') + 1]
		else:
			server_address = DEFAULT_IP_ADDRESS
	except IndexError:
		print('After \'a\' you should to point out address of the server')
		sys.exit(1)

	try:
		if '-p' in sys.argv:
			server_port = int(sys.argv[sys.argv.index('-p') + 1])
		else:
			server_port = DEFAULT_PORT
		if server_port < 1024 or server_port > 65535:
			raise ValueError
	except IndexError:
		print('After \'p\' you should to point out the number of port')
		sys.exit(1)
	except ValueError:
		print('Enter from 1024 to 65535')
		sys.exit(1)
		
	transport = socket.socket()
	transport.connect((server_address, server_port))
	message_to_server = create_presence()
	send_message(transport, message_to_server)
	try:
		answer = process_ans(get_message(transport))
		print(answer)
	except (ValueError, json.JSONDecodeError):
		print('Decode message error')
	
	return server_address, server_port

if __name__ == '__main__':
	main()
	
		
		

