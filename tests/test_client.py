import time
import unittest
import socket
from my_project.settings.utils import get_message, send_message
from my_project.client.client import process_ans, create_presence
from my_project.settings.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, RESPONSE


class UtilsTestCase(unittest.TestCase):
	
	def setUp(self):
		self.transport = socket.socket()

	def test_create_presence(self):
		self.message_to_server = create_presence()
		self.assertIsInstance(self.message_to_server, dict)
		self.assertEqual(self.message_to_server['action'], 'presence')
		self.assertIsInstance(self.message_to_server['time'], str)
		self.assertEqual(self.message_to_server['user']['account_name'], 'Guest')
		self.transport.close()
		
	def test_get_time(self):
		self.message_to_server = create_presence()
		time_1 = self.message_to_server['time']
		time.sleep(1)
		self.message_to_server = create_presence()
		time_2 = self.message_to_server['time']
		self.assertNotEqual(time_1, time_2)
		self.transport.close()

	def test_process_ans(self):
		server_address, server_port = DEFAULT_IP_ADDRESS, DEFAULT_PORT
		self.transport.connect((server_address, server_port))
		self.message_to_server = create_presence()
		send_message(self.transport, self.message_to_server)
		self.answer = get_message(self.transport)
		self.assertEqual(self.answer[RESPONSE], 200)
		self.transport.close()
