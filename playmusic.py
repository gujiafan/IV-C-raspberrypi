import os
import multiprocessing
import threading
import subprocess
from time import sleep
import signal
import psutil

def play_music(filename):
    os.system("omxplayer -o local "+filename)

fileName="Never Grow Old - The Cranberries.m4a"
new="Never_Grow_Old_-_The_Cranberries.m4a"
'''
def kill_p(parent_pid, sig=signal.SIGKILL):
    try:
        p=psutil.Process(parent_pid)
    except psutil.error.NoSuchProcess:
        return

    child_pid=p.get_child(recursive=True)
    for pid in child_pid:
        os.kill(pid.pid, sig)

p=subprocess.Popen("omxplayer -o local Never_Grow_Old_-_The_Cranberries.m4a", shell=True)
print 'Start playing'
sleep(10)
print 'Try to kill'
kill_p(p.pid)
p.terminate()
'''
