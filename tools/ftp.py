#!/usr/bin/python3
# -*- coding : utf8 -*-

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from ftplib import FTP
import os


def _ftp_return_success(ret_string):
    if ret_string[0:3] == "220" or ret_string[0:3] == "230" or ret_string[0:3] == "250" or ret_string[0:3] == "226":
        return True
    return False


def ftp_server_start(ip, port, root_dir, usr, pwd):
    # 实例化虚拟用户，这是FTP验证首要条件
    authorizer = DummyAuthorizer()
    # 添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
    authorizer.add_user(usr, pwd, root_dir, perm='elr')

    ftp_handler = FTPHandler
    ftp_handler.authorizer = authorizer

    ftp_server = FTPServer((ip, port), ftp_handler)
    ftp_server.serve_forever()


def ftp_download(ip, port, usr, pwd, src_file, dst_file):
    ftp_obj = FTP()
    ret = ftp_obj.connect(ip, port)
    if not _ftp_return_success(ret):
        return ""

    ret = ftp_obj.login(usr, pwd)
    if not _ftp_return_success(ret):
        return ""

    ret = ftp_obj.cwd(os.path.dirname(src_file))
    if not _ftp_return_success(ret):
        return ""

    if os.path.exists(dst_file):
        os.remove(dst_file)
    target_name = os.path.split(src_file)[-1]
    file_obj = open(dst_file, "wb")
    ret = ftp_obj.retrbinary("RETR " + target_name, file_obj.write, 4096)
    file_obj.close()
    if not _ftp_return_success(ret):
        os.remove(dst_file)
        return ""
    return os.path.abspath(dst_file)


if __name__ == "__main__":
    path = os.getcwd() + "/" + "root"
    ftp_server_start("127.0.0.1", 1989, path, "xzy", "xzy")

    print(ftp_download("127.0.0.1", 1989, "xzy", "xzy", "xx/Hash.exe", "./xx.exe"))