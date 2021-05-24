import sys
import logging.handlers
import logging
import os
from common.variables import LOGGING_LEVEL

LOG = logging.getLogger('server')

LOG_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(LOG_PATH, 'server_log_files/server.log')

FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

LOG_FILE = logging.handlers.TimedRotatingFileHandler(LOG_PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(FORMATTER)

LOG.addHandler(LOG_FILE)
LOG.addHandler(logging.StreamHandler(sys.stdout))
LOG.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    LOG.critical('Critical error debugging')
    LOG.error('Error debugging')
    LOG.debug('Debugging information')
    LOG.info('Information message debugging')
