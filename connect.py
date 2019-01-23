import socket
import SocketServer
import os
import thread

host="192.168.137.185"
port=8888
bufsize=1024
ADDR=(host, port)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)

while True:
    print("waiting for connection...")
    connect, addr=s.accept()
    print("connected from:", addr)
    while True:
        data=connect.recv(bufsize)
        print(data)

        if data=="song":
            connect.send("success1")
            print("song")

        if data=="photo":
            connect.send("success2")
            print("photo")
        

    connect.close()
s.close()
