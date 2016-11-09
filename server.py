import socket
import threading
import os

run = True
max = 10
address = "10.62.0.213"
port = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def handleClient(number,conn):
    receiving = True
    while receiving:
        data = conn.recv(1024)
        if data == "HELO text\n":
            print number, "HELO text\nIP:%s\nPort:%d\nStudentID:13332863\n" %(address,port)
        elif data == "KILL_SERVICE\n":
            print "Killing Service"
            sock.close()
            print "Socket closed"
            os._exit(1)
        elif not data:
            receiving = False
        else:
            print number, data


sock.bind((address,port))
print "Socket created at IP:%s and port:%s, now listening for clients" %(address,port)
sock.listen(5)
while run:
    conn, addr = sock.accept()
    threading.Thread(target = handleClient, args =(current,conn,)).start() 
