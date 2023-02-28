from socket import *
serverPort = 12010

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('The server is ready to recieve')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizeSentence = sentence.upper()
    connectionSocket.send(capitalizeSentence)
    
    connectionSocket.close()