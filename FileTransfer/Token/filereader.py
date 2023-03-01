

ip = "10.10.10.10"
port = 710
token = 10001
static = ["127.0.0.1" , "12075" ,"40910"]

f=open("token.txt","r")
lines= f.readlines()
count = 0
for line in lines:
    count +=1
cutlines=static[2].split(",")
print(cutlines)    
f.close

print (lines)
print ("lines in file",count)
with open("newtoken.txt","w") as f:
        for x in range(count):
            print(lines[x].strip(),file=f)
        #if statement checking to see if token is already in file
        print(ip,",",port,",",token,file=f)




