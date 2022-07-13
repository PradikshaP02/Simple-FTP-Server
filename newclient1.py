import socket
import threading
import os

def task1():
    conn=s
    while True:
        message = conn.recv(1024).decode()
        message = conn.recv(1024).decode()
        temp = conn.recv(1024).decode()
        filename=temp
        filesize=int(conn.recv(1024).decode())
        print('message:',message)
        print('filename:',filename)
        print('size:',filesize)

        f=open('new_'+(filename),'wb')
        data=conn.recv(1024)
        totalRecv = len(data)
        f.write(data)
        while totalRecv < filesize:
            data = s.recv(1024)
            totalRecv += len(data)
            f.write(data)
        print("Download complete")
        f.close()

def task2():
    while True:
        cli=input('Enter client id to send : ')
        filename =input('Enter file name : ')

        flag=1
        while(flag):
            if(os.path.exists(filename)):
                flag=0
            else:
                filename=input('Filename doesnt exist')

        s.send(cli.encode())
        s.send(filename.encode())
        s.send(str(os.path.getsize(filename)).encode())

        with open(filename , 'rb') as f:
                 bytesToSend = f.read(1024)
                 s.send(bytesToSend)
                 while bytesToSend != "":
                     bytesToSend = f.read(1024)
                     s.send(bytesToSend)
        f.close()


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port= 12345

s.connect((host,port))
print('connection sent\n')

t1=threading.Thread(target = task1,name='t1')
t2=threading.Thread(target = task2,name='t2')

t1.start()
t2.start()

t1.join()
t2.join()

                    
        
