
print("enter peer number/s which you want to connect to, if more than one add a , between the numbers")
numbers = input("")

numberssplit = numbers.split(",")
print(numberssplit)
number= list(map(int,numberssplit))
print (number)
numbercorrected = [x - 1 for x in number]
print(numbercorrected)


store=[]
y=0
file =  open("token.txt")
for pos, l_num in enumerate(file):
    # check if the line number is specified in the lines to read array
    if pos in numbercorrected:
        # print the required line number
        store.append(l_num.strip("\n"))
        print(store)
        y=y+1

storage =[]
for z in range(y):
    temp = store[z].split(",")
    storage.extend([temp[0],temp[1]])
print(storage)

ipfull=[]
for i in range(y):
    ipfull.append(storage[0+(i*2)])

print(ipfull)

portfull=[]
for j in range(y):
    portfull.append(storage[1+(j*2)])
print (portfull)