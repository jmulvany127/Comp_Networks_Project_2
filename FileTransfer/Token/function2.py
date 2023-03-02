
#gets ip + port from token.txt
def ip_fetcher(token):
    f=open("token.txt","r")
    lines= f.readlines()
    count = 0
    for line in lines:
        count+=1
    f.close
    #print ("lines in token",count)
    with open ('token.txt',"r+") as f:
            content =f.readline()
            #print(content)
            i=0
            for i in range((count)-1):
                content=f.readline()
                contentsplit = content.split(",")
                tkn = int(contentsplit[2])
                #print(tkn)
                #print(int(token))
                if int(token) == tkn :
                    print("Token is in database")
                    storage = [contentsplit[0],contentsplit[1]]
                    f.close
                    print (storage)
                    return storage  
            print("token was not found in database")  
            

ip_fetcher(1939721501944343189)
