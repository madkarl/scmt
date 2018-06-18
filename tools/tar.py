#!/usr/bin/python3
# -*- coding : utf8 -*-

import os
import tarfile


def dir_to_tar(src_path, dst_path, dst_name=None):
    """
    将目录打包为tar.gz文件
    :param src_path: 被打包目录
    :param dst_path: tar文件存放目录
    :param dst_name: tar文件名
    :return: tar.gz生成路径
    """
    if not os.path.exists(src_path):
        return ""
    if not dst_name or "" == dst_name:
        dst_name = os.path.basename(src_path) + ".tar.gz"
    if not dst_name.find(".tar.gz"):
        dst_name += ".tar.gz"
    tar_path = dst_path + "/" + dst_name
    if os.path.exists(tar_path):
        os.remove(tar_path)

    tar_obj = tarfile.open(tar_path, "w:gz")
    tar_obj.add(src_path, arcname=os.path.basename(src_path))
    tar_obj.close()
    return os.path.abspath(tar_path)


def tar_to_dir(src_file, dst_path):
    if not os.path.exists(src_file):
        return ""
    tar_obj = tarfile.open(src_file, "r:gz")
    file_names = tar_obj.getnames()
    tar_obj.extractall(dst_path)
    return dst_path + "/" + file_names[0]


if __name__ == "__main__":
    src = "D:\\Desktop\\enviroment\\hive-1.1.0-cdh5.10.0"
    dst = "."
    tar = "test.tar.gz"
    ret = dir_to_tar(src, dst, tar)
    print("fn_ret:", ret)

    src = "./test.tar.gz"
    dst = "d:"
    ret = tar_to_dir(src, dst)
    print("fn_ret:", ret)
