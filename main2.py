import socket
import SocketServer
import os
import thread
import recognizer
import song
import copy
import signal
import multiprocessing
import subprocess

def recv_file(bufsize):
    global data
    data=connect.recv(bufsize)

host="192.168.137.38"
port=8888
signalsize=1
bufsize=1025
ADDR=(host, port)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)

photo_num=0
flag=0

while True:
    print("Waiting for connection...")
    connect, addr=s.accept()
    print("Connected from:", addr)
    
    mode=connect.recv(signalsize)
    print str(mode)
	
    if str(mode) == '0': ###enter music mode
	print("Receiving song...")
	f=open('file_recvd.wav', 'wb')
	while True:
	    try:
		data=connect.recv(bufsize)
	    except:
		break
	    if not data:
		break
	    f.write(data)
	f.close()
	print("File received.")
        connect.close()
	recog=0
	print("Start recognizing...")
	try:
            result=recognizer.recognize("file_recvd.wav")
            recog=1
            print("Found")
        except:
            print("Not found")
	
        print("Waiting for connection...")
        connect, addr=s.accept()
        print("Connected from:", addr)

	if recog == 1:
            songName=result
            songName.encode("GB2312")
            connect.send(songName)
            connect.close()
            continue
        else:
            connect.send("Not found")
            connect.close()
            continue
		
    elif str(mode) == '1': ###enter photo mode
	photo_num=photo_num+1
	print("Receiving photo...")
	f=open('photo_recvd'+str(photo_num)+'.jpg', 'wb')
        while True:
	    try:
	        data=connect.recv(bufsize)
                print(len(str(data)))
	    except:
                print "Error occures, break."
	        break
	    if not data:
		print "File empty, break."
                break
	    f.write(data)
            print('.')
	f.close()
	print("File received.")
        connect.close()
        print("Waiting for connection...")
        connect, addr=s.accept()
        print("Connected from:", addr)
        connect.send("SUCCESS")
	connect.close()
	continue
	
    elif str(mode) == '2': ###enter download & play music mode
	data=connect.recv(bufsize)
        songName=str(data)
        print("Song name is:", songName)
        print("Downloading", songName)
	fileName=song.download(songName)
        fileName.replace('u\'','\'')
        fileName=str(fileName)
        print(type(fileName))
        old=copy.copy(fileName)
        new=copy.copy(fileName)
        new=new.replace(' ', '_')
        os.rename(old, new)
        print(new, type(new))
        connect.send("SUCCESS") 
        connect.close()

        if flag==1:
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
            #p.terminate()
        
        p=subprocess.Popen("omxplayer -o local "+new, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        print "Start playing"
        flag=1

        continue

    connect.close()
		
s.close()
