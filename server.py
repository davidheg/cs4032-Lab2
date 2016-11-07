
import socket
import sys

def openSocket(address,port):
	
    return;


def main():
    address = "10.62.0.213"
    port = 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((address,port))
    sock.listen(10)
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print data
 
main()
