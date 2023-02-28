from socket import *
import sys


serverPort =12075
SEPARATOR = "<SEPARATOR>"
mytoken=10001
serverSocket = socket (AF_INET,SOCK_STREAM)

serverSocket.bind (('',serverPort))
serverSocket.listen(1)
print("the server is ready to recieve")

#ipAddr=serverSocket.getsockname()

#def mydata()


while 1:
    connectionSocket,addr = serverSocket.accept()
    received = connectionSocket.recv(65536).decode()
    port, token = received.split(SEPARATOR)
    print (addr[0], port, token)
    with open("token.txt","w") as f:
       sys.stdout = f
       print("Ip",addr[0],"Port", port, "Token",token)
    exit()

serverSocket.close
