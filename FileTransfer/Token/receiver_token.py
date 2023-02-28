from socket import *
import sys
import os.path

serverPort =12075
SEPARATOR = "<SEPARATOR>"
mytoken=10001




serverSocket = socket (AF_INET,SOCK_STREAM)
serverSocket.bind (('',serverPort))

with open ("mytoken.txt","w") as my:
        print(mytoken,file=my)
        my.close()

serverSocket.listen(1)
print("the server is ready to recieve")

#ipAddr=serverSocket.getsockname()

#def mydata()
#i dont know what your path is
path =("C:\\CSU23021\\Comp_Networks_Project_2\\FileTransfer\\Token\\token.txt")
#print(os.path.isfile(path))
while 1:
    connectionSocket,addr = serverSocket.accept()
    received = connectionSocket.recv(65536).decode()
    port, token = received.split(SEPARATOR)
    #if token doesnt exist write here rn
    if os.path.isfile(path) != True:
        with open("token.txt","w") as f:
            print(addr[0],",", port,",",token,file=f)
            f.close
            exit()
    #else if it does exist read token values and compare against ones in db,if it doesnt exist add it.
    else:
        with open ('token.txt',"r+") as f:
            content =f.readline()
            #print (content)
            contentsplit = content.split(",")
            tkn = int(contentsplit[2])
            print(tkn)
            print(int(token))
            if int(token) == tkn :
                print("Token is in database")
                f.close  
        
    with open("token.txt","r+") as f:
        print(addr[0],",", port,",",token,file=f)
        f.close
        print("token.txt was written to")
exit()
    
serverSocket.close