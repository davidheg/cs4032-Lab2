import socket
import threading
import os
import sys

run = True
max = 10
address = "10.62.0.213"
port = int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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
    conn, addr = sock.accept()
    threading.Thread(target = handleClient, args =(conn,addr,)).start()

