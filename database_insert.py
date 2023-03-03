import os.path
path = "DATABASE.txt"



#status = "miss,missbutfound,found,foundbut..."


#person = [apperance ,name, last seen, status]

#if anything is unknown, it needs to be empty,
# add to database file#input line required
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
            
database_insert()