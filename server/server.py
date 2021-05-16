import json
import socket
import sys

from my_project.settings.utils import get_message, send_message
from my_project.settings.variables import (ACCOUNT_NAME, ACTION, DEFAULT_PORT,
	ERROR, MAX_CONNECTIONS, PRESENCE,
	RESPONSE_DEFAULT_IP_ADDRESS, RESPONSE, TIME, USER)

def process_client_message(message):
	if (ACTION in message and
		message[ACTION] == PRESENCE and
		TIME in message and
		USER in message and
		message[USER][ACCOUNT_NAME] == 'Guest'):
		return {RESPONSE: 200}
	return {RESPONSE_DEFAULT_IP_ADDRESS: 400, ERROR: 'Bad Request.'}


def main():
	try:
		if '-a' in sys.argv:
			listen_address = sys.argv[sys.argv.index('-a') + 1]
		else:
			listen_address = ''
	except IndexError:
		print('After \'a\' you should to point out address of the server')
		sys.exit(1)
	
	try:
		if '-p' in sys.argv:
			listen_port = int(sys.argv[sys.argv.index('-p') + 1])
		else:
			listen_port = DEFAULT_PORT
		if listen_port < 1024 or listen_port > 65535:
			raise ValueError
	except IndexError:
		print('After \'p\' you should to point out the number of port')
		sys.exit(1)
	except ValueError:
		print('Enter from 1024 to 65535')
		sys.exit(1)

	transport = socket.socket()
	transport.bind((listen_address, listen_port))
	transport.listen(MAX_CONNECTIONS)
	
	while True:
		client, client_address = transport.accept()
		try:
			message_from_client = get_message(client)
			print(message_from_client)
			response = process_client_message(message_from_client)
			send_message(client, response)
			client.close()
		except (ValueError, json.JSONDecodeError):
			print('Invalid message received')
			client.close()
			
if __name__ == '__main__':
	main()
