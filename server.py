import socket
import threading
import os
import sys

run = True
max = 10
address = "10.62.0.213"
port = int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
threadpool = []
numberofThreads = 0

def sortThreadPool():
        i = 0
        for thread in threadpool:
                if(not thread.isAlive()):
                        threadpool.pop(i)
                        global numberofThreads
                        numberofThreads = numberofThreads - 1
                i = i + 1
        threadpool.sort()

def handleClient(conn,addr):
    receiving = True
    while receiving:
        data = conn.recv(1024)
        if "HELO" in data:
            conn.send("%sIP:%s\nPort:%d\nStudentID:13332863\n" %(data,address,port))
        elif data == "KILL_SERVICE\n":
            print "Killing Service"
            sock.close()
            print "Socket closed"
            os._exit(1)
        elif not data:
            receiving = False
        else:
            print data

sock.bind((address,port))
print "Socket created at IP:%s and port:%d, now listening for clients" %(address,port)
sock.listen(5)
while run:
    if numberofThreads < max:
        conn,addr = sock.accept()
        threadpool.append(threading.Thread(target = handleClient, args =(conn,addr,)))
        threadpool[numberofThreads].start()
        global numberofThreads
        numberofThreads = numberofThreads + 1
    else:
        print "There are no free threads"
    threading.Thread(target = sortThreadPool).start()
