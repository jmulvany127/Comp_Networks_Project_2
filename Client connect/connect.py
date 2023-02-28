import socket
import os
import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 65536

host = "127.0.0.1"
port = 5001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))
#print("[+] Connected to ", host)

#filename goes to your directory for the file
filedirectiory=("C:\\ComputerNetworks\\file transfer\\")
filename = ("masterpiece.png")

filepath = ("C:\\ComputerNetworks\\file transfer\\masterpiece.png")
print (filepath)
print (os.path.exists(filepath))

filesize = os.path.getsize(filepath)
print (filesize)
s.send(f"{filepath}{SEPARATOR}{filesize}".encode())
#file = open(filepath, 'wb') 

progress = tqdm.tqdm(range(filesize), f"Sending {filepath}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filepath, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
s.close()
