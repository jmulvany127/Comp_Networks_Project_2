from socket import *
import json
import random
serverName = "127.0.0.1"
Port = 12075

clientSocket = socket (AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,Port))
#token = random.randint(10000,99999)
token=10000
SEPARATOR = "<SEPARATOR>"
clientSocket.send(f"{Port}{SEPARATOR}{token}".encode())
print(Port,token)