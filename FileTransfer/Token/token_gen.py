import random
import os.path
import string
path ="machine_token.txt"
string.ascii_letters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def token_gen():
     x = hash(round(random.uniform(10000,99999),4))
     print(x)
     y=abs(hash(random.choice(string.ascii_letters)))
     print(y)
     w=x*y
     print(w)
     token = int( w)
     return (token)


def token_insert():
    if os.path.isfile(path)!= True:
        with open(path,"w") as f:
            token = token_gen()
            print(token,file=f)
            f.close
            print(token)
            return (token)
    else:
        with open(path,"r") as f:
            token = f.readline()
            f.close
            print("read from file",token)
            return ((token))
        
print(token_gen())
print(token_insert())