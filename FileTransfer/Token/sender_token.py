from socket import *
import json

serverName = "127.0.0.1"
Port = 12075

clientSocket = socket (AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,Port))
token = 10000
SEPARATOR = "<SEPARATOR>"
clientSocket.send(f"{Port}{SEPARATOR}{token}".encode())
