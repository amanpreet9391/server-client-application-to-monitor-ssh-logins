import socket
import subprocess
import sys
import threading
import time
from queue import Queue


NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_sessions = []
all_address = []



# Create the socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 12345
        s=socket.socket()
    except socket.error as e:
        print("Error while reating socket: "+ str(e))

# Socket binding and listening the new connections
def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)

    except socket.error as e:
        print("Socket binding error: " + str(e))
        bind_socket()

def accept_connection():

    for i in all_sessions:
        i.close()
    del all_sessions[:]
    del all_address[:]

    

    ##command
    while True:
        session,address =  s.accept()
        s.setblocking(1) # prevents disconnecting from server because of time out

        all_address.append(address)
        all_sessions.append(session)

        print("Connection has been established")

        ##See all the connected clients and select any client

        # data = session.recv(2048).decode()
        # # if not data:
        # #     # if data is not received break
        # #     break
        # print("From the connected client: " + str(data))
        #data=input('-->')
        #session.send(data.encode())


    session.close()

def list_connections():
    results=''
    for i, session in enumerate(all_sessions):
        try:
            session.send(str.encode(' '))
            session.recv(20480)
        except:
            del all_sessions[i]
            del all_address[i]
            continue

        results = results + str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n" 
        #print(results)
    print("----Clients----" + "\n" + results)


def get_connection(cmd):
    try:
        target = cmd.replace('select ', '')  # target = id
        target = int(target)
        conn = all_sessions[target]
        print("You are now connected to :" + str(all_address[target][0]))
        return conn
    except:
        print("Selection not valid")
        return None

def get_status(session):
    while True:
        data = session.recv(20480).decode()
        print("From the connected client: " + str(data))

        



def shell():
    
    while True:
        cmd = input("--> ")
        if cmd=='list':
            list_connections()
        elif 'select' in cmd:
            session = get_connection(cmd)
            if session is not None:
                get_status(session)
        else:
            print("use list or select")        



# def main():
#     create_socket()
#     bind_socket()
#     accept_connection()

# main()
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connection()
        if x == 2:
            shell()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
create_jobs()







