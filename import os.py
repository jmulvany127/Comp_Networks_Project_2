import os.path






path = "C:\\CSU23021\\Comp_Networks_Project_2\\Final_v1\\Node_1\DataBase_A\\DATABASE.txt"



status = "miss,missbutfound,found,foundbut..."


person = [apperance ,name, last seen, status]

#if anything is unknown, it needs to be empty,
# add to database file#input line required
def database_insert(apperance,name,seen_last, status):
    #if token doesnt exist write here rn
        if os.path.isfile(path) != True:
            with open("DATABASE.txt","w") as f:
                print("People:",file=f)
                print("Apperance, Name, Last Seen, Status",file=f)
                f.close
                return
    #else if it does exist read token values and compare against ones in db,if it doesnt exist add it.
        else:
            f=open("DATABASE.txt","r")
            lines= f.readlines()
            count = 0
            for line in lines:
                count +=1
            f.close
            with open ('DATABASE.txt',"r+") as f:
                input ("do you wish to add to database (y/n):")
                if (input == y):
                     input("type in the persons Apperance,If this is unkown, leave this section blank",apperance)
                     input("type in the persons name,If this is unkown, leave this section blank",name)
                     input("type in the persons name,If this is unkown, leave this section blank",seen_last)
                     input("type in the persons name,If this is unkown, leave this section blank",status)
                for x in range(count):
                    print(lines[x].strip(),file=f)
                print(apperance,name,seen_last,status)
                print()
                f.close
                print("Database was written to")
                #print(token)
                return
            