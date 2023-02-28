from connectiondefinition import send__file
import socket
import os
import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 65536

host = "127.0.0.1"
port = 5001

#s = socket.socket()
#s.connect((host, port))
#print("[+] Connected to ", host)

#filename goes to your directory for the file
filename = "C:\\ComputerNetworks\\file transfer\\masterpiece.png"
print (os.path.exists(filename))
send__file(host,port,filename)





""""
filesize = os.path.getsize(filename)
print (filesize)
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
#file = open(filename, 'wb') 

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
s.close()
"""