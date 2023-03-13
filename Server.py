import socket
import _thread as thread
import os


def client_thread(conn,addr):
    conn.send(bytes('Welcome to chat'.encode()))
    x = len(lst)
    while True:
        client = conn.recv(1024).decode()
        temp = filename = conn.recv(1024).decode()
        filesize = int(conn.recv(1024).decode())
        f = open('new_' + (filename), 'wb')
        data = conn.recv(1024)
        total_recv = len(data)
        f.write(data)
        while total_recv < filesize:
            data = conn.recv(1024)
            total_recv += len(data)
            f.write(data)
        print("Download Complete!")
        f.close()
        broadcast(client, str(x), temp)

def broadcast(msg,cli,filename):
    if(msg != 'b' and msg != 'B'):
        s = lst[int(msg)-1]
        s.send(cli.encode())
        print('From: ',cli,filename)
        s.send(filename.encode())
        print('Size: ',os.path.getsize(filename))
        s.send(str(os.path.getsize(filename)).encode())

        with open(filename, 'rb') as f:
            bytes_to_send = f.read(1024)
            s.send(bytes_to_send)
            while bytes_to_send != "":
                bytes_to_send = f.read(1024)
                s.send(bytes_to_send)
        f.close()
    else:
        for i in lst:
            if i!= lst[int(cli)-1]:
                s=i
                s.send(cli.encode())
                print('From: ',cli,filename)
                s.send(filename.encode())
                print('Size: ',os.path.getsize(filename))
                s.send(str(os.path.getsize(filename)).encode())

                #sending file
                with open(filename,'rb') as f:
                    bytes_to_send = f.read(1024)
                    s.send(bytes_to_send)
                    while bytes_to_send != "":
                        bytes_to_send = f.read(1024)
                        s.send(bytes_to_send)
                f.close()

    os.remove(filename)


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

server.bind((host,port))
server.listen(100)
print("Server Started...")

lst = []

while True:
    conn,addr = server.accept()
    print("Client connected : [" +str(addr) + "]")
    lst.append(conn)
    thread.start_new_thread(client_thread,(conn,addr))

server.close()
