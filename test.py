import psutil
import subprocess
import signal
from time import sleep
import os

fileName="Never_Grow_Old_-_The_Cranberries.m4a"

p=subprocess.Popen("omxplayer -o local "+fileName, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
print 'Start playing'
sleep(10)
print 'Try to kill'
os.killpg(os.getpgid(p.pid), signal.SIGTERM)
#p.kill()
print 'success'
