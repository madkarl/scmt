#!/usr/bin/python3
# -*- coding:utf8 -*-


from tools import log
import setproctitle
import os

logger = log.get_logger()
DEPLOY_TEMP_DIR = ""

def deploy_initialize():
    setproctitle.setproctitle("SCMT-DEPLOY")
    log.conf_logger("scmt-deploy")
    DEPLOY_TEMP_DIR = os.tem


def deploy_zookeeper(template_path, config_file):
    print("template_path:", template_path)
    print("config_file:", config_file)


if __name__ == "__main__":
    deploy_initialize()
    deploy_zookeeper("zookeeper-bin", )
