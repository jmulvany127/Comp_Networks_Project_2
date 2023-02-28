import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 65536

s = socket.socket()
host = "127.0.0.1"
port = 5001
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected to ", host)
#print (os.path.exists("C:\\ComputerNetworks\\Python-Sockets-File-Transfer-master\\Python-Sockets-File-Transfer-master\\masterpiece.png"))
filename = "C:\\ComputerNetworks\\file transfer\\masterpiece.png"
#file = open(filename, 'wb') 
print (os.path.getsize(filename))
filesize = os.path.getsize(filename)
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