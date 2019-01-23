#coding: utf-8
import socket
import SocketServer
import os
import thread
import recognizer
import song

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
    connect.send("connected")
    flag=1
    f=open('file_recvd.wav', 'wb')
    while True:
        try:
            data=connect.recv(bufsize)
            '''
            if not data or len(data) == 0:
            print("file not received")
            break
            else:
            print("file received")
            '''
        except:
            break
        f.write(data)
    f.close()
    print("file received") 
    connect.close()
    print("Start recognize...")
    recog=0
    
    try:
        result=recognizer.recognize("new_apple.m4a")
        recog=1
        print("found")
    except:
        print("not found")
    
    connect, addr=s.accept()
    print("connected from:", addr)
    if recog==1:
        songName=result
        songName.encode("GB2312")
        connect.send(songName)
        connect.close()
        continue
    else:
        connect.send("not found")
        connect.close()
        continue
    '''
    connect, addr=s.accept()
    print("connected from:", addr)
    string=""
    while True:
        try:
            data=connect.recv(bufsize)
        except:
            break
        string=string+data
    print("song name reveived")
    connect.close()

    song_name=song.download(string)
    '''
    if flag==1:
        break
s.close()
