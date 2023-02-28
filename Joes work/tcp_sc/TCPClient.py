from socket import*
serverName = '127.0.0.1'
serverPort = 12010

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence:').encode('utf-8')

clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(2048)

print(('From Server: '), modifiedSentence.decode('utf-8'))

clientSocket.close()