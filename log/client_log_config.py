import os
import logging
import sys
from common.variables import LOGGING_LEVEL

LOG = logging.getLogger('client')

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

LOG_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(LOG_PATH, 'client_log_files/client.log')

LOG_FILE = logging.FileHandler(LOG_PATH, encoding='utf8')
LOG_FILE.setFormatter(FORMATTER)

LOG.addHandler(LOG_FILE)
LOG.addHandler(logging.StreamHandler(sys.stdout))
LOG.setLevel(LOGGING_LEVEL)


if __name__ == '__main__':
    LOG.critical('Critical error debugging')
    LOG.error('Error debugging')
    LOG.debug('Debugging information')
    LOG.info('Information message debugging')
