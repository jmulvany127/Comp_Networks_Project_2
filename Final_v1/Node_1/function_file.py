import os.path


#adds name, apperance, last_seen,status into the database,
def database_insert():
    #if token doesnt exist write here rn
        if os.path.isfile("DATABASE.txt") != True:
            with open("DATABASE.txt","w") as f:
                print("People:",file=f)
                print("Name, Apperance, Last Seen, Status",file=f)
                f.close
                return
        else: 
            f=open("DATABASE.txt","r")
            lines= f.readlines()
            count = 0
            for line in lines:
                count +=1
            f.close
            with open ("DATABASE.txt","r+") as f:
                first =input ("do you wish to add to database (y/n):")
                if (first == "y"):
                     name =input("type in the persons name,If this is unkown, leave this section blank:")
                     apperance= input("type in the persons Apperance,If this is unkown, leave this section blank:")
                     seen_last =input("type in the persons last seen,If this is unkown, leave this section blank:")
                     status = input("type in the persons status,If this is unkown, leave this section blank:")
                for x in range(count):
                    print(lines[x].strip(),file=f)
                print(name,apperance,seen_last,status,file=f)
                print()
                f.close
                print("Database was written to")
                #print(token)
                return

























###i was able to get this function to work combined with sender_token sending into receiver_token. I think it works
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









#turns token value into ip address and port value by reading token.txt
def ip_fetcher(token):
    f=open("token.txt","r")
    lines= f.readlines()
    count = 0
    for line in lines:
        count+=1
    f.close
    #print ("lines in token",count)
    with open ('token.txt',"r+") as f:
            i=0
            for i in range((count)-1):
                content=f.readline()
                contentsplit = content.split(",")
                tkn = int(contentsplit[2])
                #print (f"token {token}")
                #print(f"tkn {tkn}")
                #print(int(token))
                if int(token) == tkn :
                    print("Token is in database")
                    storage = [contentsplit[0],contentsplit[1]]
                    f.close
                    #print (storage)
                    return storage  
            print("Token is invalid,peer has been rejected")  
            return False


#function checks to see if the input is a postive,whole number and that number has an associated address attached to it.
def number_check(number):
    try:
        f=open("token.txt","r")
        lines= f.readlines()
        count = 0
        for line in lines:
            count +=1
        f.close
        numbe = int(number)  
        if numbe <=0 :
            print("Input must be postive")
            return False
        elif numbe >count:
            print("There is no peer address saved with this input")
            return False
        else:
            return True
    except ValueError:
        print("Input needs to be a postive, whole number to work")
        return False


#fuction checks token.txt and will go to line inputted and store the ip and port number from that line in storage
def addres_arrays(numbercorrected):
    store=[]
    y=0
    file =  open("token.txt")
    for pos, l_num in enumerate(file):
        # check if the line number is specified in the lines to read array
        if pos in numbercorrected:
            # print the required line number
            store.append(l_num.strip("\n"))
            #print(store)
            y=y+1
    storage =[]
    for z in range(y):
        temp = store[z].split(",")
        storage.extend([temp[0],temp[1]])
    #print(storage)
    return storage

#stores array of peer tokens from file for access
def token_arrays(numbercorrected):
    store=[]
    y=0
    file =  open("token.txt")
    for pos, l_num in enumerate(file):
        # check if the line number is specified in the lines to read array
        if pos in numbercorrected:
            # print the required line number
            store.append(l_num.strip("\n"))
            #print(store)
            y=y+1
    storage =[]
    for z in range(y):
        temp = store[z].split(",")
        storage.extend([temp[2]])
    #print(storage)
    return storage

#return local token number from list 
def get_my_token(my_p_num):
    my_p_num =str(my_p_num)
    correctnums =splitting(my_p_num)
    storage = []

    storage = token_arrays(correctnums)

    return storage[0]

#function that breaks storage down and gives the ip address that is necessary
def ip_array(storage):
    global ipfull
    ipfull=[]
    y = len(storage)-1
    for i in range(y):
        ipfull.append(storage[0+(i*2)])
    return ipfull

#function that breaks storage down and gives the necessary port number to connect to.
def port_array(storage):
    global portfull
    portfull=[]
    z= len(storage)-1
    for j in range(z):
        portfull.append(storage[1+(j*2)])
    return portfull


#subtracts one from the input value,
def splitting(numbers):
    numberssplit = numbers.split(",")
    number= list(map(int,numberssplit))
    numbercorrected = [x - 1 for x in number]
    return numbercorrected




"""
#function 1 example
def main():
    print("enter peer number which you want to connect to")
    numbers = input("")
    peer_to_ip_and_port(numbers)
    print(portfull,ipfull)
main()
"""