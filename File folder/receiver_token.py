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

ipAddr=serverSocket.getsockname()
connectionSocket,addr = serverSocket.accept()
received = connectionSocket.recv(65536).decode()
port, token = received.split(SEPARATOR)



print("the 3",addr[0],port,token)

#i dont know what your path is
#path =("C:\\CSU23021\\Comp_Networks_Project_2\\FileTransfer\\Token\\token.txt")
#print(os.path.isfile(path))
##this could probably be turned into a function

##ip address should probably be taken from serversocket.accept, i think i see it taken from it, address[0] or something like that
#create token.txt, if token.txt already exists, it will open token.txt, if the token is already in the file it will do nothing,if the token is not in the file it will add it, it requires ip address,port,token, addr[0] was were the ip address was stored,you may need to fix this function before it works
def token_insert(ip,port,token):
    #if token doesnt exist write here rn
        if os.path.isfile("token.txt") != True:
            with open("token.txt","w") as f:
                print(ip,",", port,",",token,file=f)
                f.close
                return
    #else if it does exist read token values and compare against ones in db,if it doesnt exist add it.
        else:
            f=open("token.txt","r")
            lines= f.readlines()
            count = 0
            for line in lines:
                count +=1
            f.close
            with open ('token.txt',"r+") as f:
            #content =f.readline()
            #print(content)
                for x in range(count):
                    content=f.readline()
                    contentsplit = content.split(",")
                    tkn = int(contentsplit[2])
                    if int(token) == tkn :
                        print("Token is in database")
                        f.close
                        return
            with open("token.txt","r+") as f:
                for x in range(count):
                    print(lines[x].strip(),file=f)
                print(ip,",", port,",",token,file=f)
                f.close
                print("token.txt was written to")
                #print(token)
                return

token_insert(addr[0],port,token)
exit()