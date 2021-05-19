import sys
import logging
from my_project.log.client_log_config import logger as logger_client
from my_project.log.server_log_config import logger as logger_server
import traceback
import inspect

if sys.argv[0].find('client') == -1:
    logger = logger_server

else:
    logger = logger_client


def log(func_to_log):
    # функция декоратор
    def log_server(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        logger.info(f'Function {func_to_log.__name__} with parameters {args}, {kwargs}.'
                    f'From module {func_to_log.__module__} from'
                    f'Function {traceback.format_stack()[0].strip().split()[-1]}.'
                    f'From function {inspect.stack()[1][3]}')
        return ret

    return log_server
