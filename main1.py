import socket
import SocketServer
import os
import thread
import recognizer
import song

host="192.168.137.61"
port=8888
bufsize=1024
ADDR=(host, port)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)

while True:
    backflag=False
    print("waiting for connection...")
    connect, addr=s.accept()
    print("connected from:", addr)
    #connect.send("connected")
    
    try:
        string=connect.recv(bufsize)
    except:
        print("connection error")
        continue
    connect.close()

    if string=='music':######################################## Part of Song
        print("Start song recognization...")
        f=open('file_recvd.wav', 'wb')
        connect, addr=s.accept()
        print("Connected from:", addr)
        while True:
            try:
                data=connect.recv(bufsize) 
            except:
                break
            if data=='back':
                backflag=True
                break
            if not data:
                print('File empty, stop receiving')
                break
            f.write(data)
            print('.')
        f.close()
        print("File closed")
        connect.close()
        print("Connect closed")
        if backflag:
            print("back to main menu")
            continue
        print("file received") 
        print("Start recognize...")
        recog=0
        
        try:
            #result=recognizer.recognize("new_apple.m4a")
            result=recognizer.recognize("file_recvd.wav")
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
        print("End of part of song recognization")
        
    if string=='photo':####################################### Part of Photo
        print("Start photo uploading...")
        connect, addr=s.accept()
        print("Connected from:", addr)
        f=open('file_recvd.jpg', 'wb')
        while True:
            try:
                data=connect.recv(bufsize)
            except:
                break
            if data=='back':
                backflag=True
                break
            if not data:
                print('File empty, stop receiving')
                break
            f.write(data)
        f.close()
        connect.close()
        print("File received")
        connect, addr=s.accept()
        connect.send=("File recvd")
        if backflag:
            print("back to main menu")
            continue
        print("End of photo upload.")

s.close()
