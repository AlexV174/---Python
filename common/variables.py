DEFAULT_PORT = 7777
DEFAULT_IP_ADDRESS = '192.168.0.2'
DEFAULT_CLIENT_ID = 'UNKNOWN'
DEFAULT_USER = 'GUEST'
MAX_CONNECTIONS = 3
MAX_PACKAGE_LENGTH = 1024
ENCODING = 'utf-8'

ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

PRESENCE = 'presence'
CHAT = 'chat'
NON_PRESENCE = 'non_presence'
RESPONSE = 'response'
ERROR = 'error'
QUIT = 'quit'

DICT_ANSWER_CODE = {
    0: 'UNKNOWN',
    100: 'Base notification',
    101: 'Important notification',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    400: 'Wrong JSON-object/ wrong request',
    401: 'Not authorization',
    402: 'Not authorization',
    403: 'forbidden',
    404: 'Not found',
    409: 'Conflict',
    410: 'User offline',
    500: 'Server ERROR',
}

DEBUG = True
LOGGING_LEVEL = 'WARNING'
if DEBUG:
    LOGGING_LEVEL = 'DEBUG'
