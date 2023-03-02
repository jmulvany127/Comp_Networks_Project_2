from socket import *
import json
import random
from token_gen import token_insert
serverName = "127.0.0.1"
Port = 12075
SEPARATOR = "<SEPARATOR>"

#token shall be a random value between 10000-99999, and have 4 decimal places
token = int(token_insert())
#print (token)


clientSocket = socket (AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,Port))
clientSocket.send(f"{Port}{SEPARATOR}{token}".encode())

