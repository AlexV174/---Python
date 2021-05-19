from unittest import TestCase
import unittest
import socket
from my_project.settings.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT



class UtilsTestCase(unittest.TestCase):
	
	def setUp(self):
		self.transport = socket.socket()

	def test_process_client_message(self):
		listen_address, listen_port = DEFAULT_IP_ADDRESS, DEFAULT_PORT
		self.transport.bind((listen_address, listen_port))
		print(listen_address, listen_port)
		self.transport.close()