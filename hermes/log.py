# -*- coding: utf-8 -*-

"""
Logging setup for hermes
"""

import logging
from logging import StreamHandler, Formatter, DEBUG


def get_logger(process):
    logger = logging.getLogger(process.name)
    stream_handler = StreamHandler()
    stream_handler.setFormatter(
        Formatter('[%(asctime)s %(name)s %(levelname)s] %(message)s')
    )
    logger.setLevel(DEBUG)
    logger.addHandler(stream_handler)
    return logger


class LoggerMixin(object):
    def run(self, *args, **kwargs):
        self.log = get_logger(self)
