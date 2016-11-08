import socket
import sys
import threading
from threading import Thread

run = True
max = 10
threadPool = []
threadNumber = 0
address = "10.62.0.213"
port = 8000
StudentID = 13332863

def createThread(data):
    if len(threadPool) < max:
        thread = Thread(target = handleClient, args = [data]);
        threadPool.append(thread)
        thread.start()
    else:
        i = 0;
        while( i < len(threadPool)):
            thread = threadPool[i]
            if(not(thread.isAlive())):
                threadPool.pop(i)
        createThread(data)
    return

def handleClient(data):
    print "threads number = ", threading.activeCount()
    if data == "HELO text\n":
        print "HELO text\nIP:%s\nPort:%d\nStudentID:%d\n" %(address,port,StudentI$
    elif data == "KILL_SERVICE\n":
        global run
        run = False;
        print "Killing service"
    else:
        print data
                              
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((address,port))
    while(run):
        sock.listen(100)
        conn, addr = sock.accept()
        data = conn.recv(1024)
        createThread(data)

main()