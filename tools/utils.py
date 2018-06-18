#!/usr/bin/python3
# -*- coding : utf8 -*-

import os
import platform


def make_dir(path):
    platform_info = platform.architecture()
    is_linux = False if not platform_info[1].find("Windows") else True
    split_ch = "/" if is_linux else "\\"

    path = os.path.abspath(path)
    split_dir_name = path.split(split_ch)

    cur_dir = ""
    for x in range(0, len(split_dir_name)):
        if x == 0:
            cur_dir = "/" + split_dir_name[x] if is_linux else split_dir_name[x]
        else:
            cur_dir = cur_dir + split_ch + split_dir_name[x]

        if not os.path.exists(cur_dir):
            os.mkdir(cur_dir)