#!/usr/bin/python3
# -*- coding : utf8 -*-


import logging
try:
    import conf
    LOG_NAME = conf.LOGGER_NAME
except:
    LOG_NAME = "LOG"
    pass


def get_logger(name=None):
    if not name:
        return logging.getLogger(LOG_NAME)
    else:
        return logging.getLogger(name)


def conf_logger(name=None, level=logging.INFO, prefix="%Y-%m-%d %H:%M:%S"):
    logger = get_logger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s'))
    logger.addHandler(handler)