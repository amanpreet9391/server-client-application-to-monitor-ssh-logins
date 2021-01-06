import socket
import os
import subprocess

s=socket.socket()


host='134.209.152.185'
#host = 'localhost'
#host = '192.168.0.104'
port=12345

s.connect((host,port))
data = s.recv(1024)


while True:
    f = subprocess.Popen(['tail','-F','/app/test','|','grep', 'sshd '],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    while True:
        line = f.stdout.readline()
        print (line)
        client_data=str(line)
        s.send(client_data.encode())
s.close()            
