
import socket
import sys

def openSocket(address,port):
	
    return;


def main():
    address = "10.62.0.213"
    port = 8000
    #openSocket(address,port);
    sock = socket.socket()
    sock.listen()
    data = sock.recv(1024)
    print data
    
if __name__ == "__main__":main() ## with if
