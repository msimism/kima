""" Logger module to handle logging configuration """

import logging
import sys

class Logger:
    def __init__(self, name, level=logging.INFO, log_file=None, debug_modules=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # File handler
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(level)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        # Debug modules
        if debug_modules:
            self.setup_debug_modules(debug_modules, formatter)

    def setup_debug_modules(self, debug_modules, formatter):
        for module in debug_modules:
            module_logger = logging.getLogger(module)
            module_logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(logging.DEBUG)
            handler.setFormatter(formatter)
            module_logger.addHandler(handler)

    def get_logger(self):
        return self.logger
