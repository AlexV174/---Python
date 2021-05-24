import traceback


def log_de(f):
    def corator(self, *args, **kwargs):
        self.logger.debug(f'Function {f.__name__} ({args}, {kwargs}) from'
                          f'{traceback.format_stack()[0].strip().split()[-1]} logger')

        return f(self, *args, **kwargs)

    return corator
