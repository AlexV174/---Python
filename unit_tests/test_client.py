import unittest

from client import Client


class TestClass(unittest.TestCase):
    def test_not_default_account_name(self):
        client = Client('NotGuest')
        self.assertNotEqual(client.account_name, 'GUEST', 'Name not recognized')

    def test_inst_create(self):
        client = Client()
        self.assertEqual(client.addr, '192.168.0.2', 'IP address not received')
        self.assertEqual(client.port, 7777, 'Port not received')


if __name__ == '__main__':
    unittest.main()
