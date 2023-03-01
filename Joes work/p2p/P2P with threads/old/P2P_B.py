import socket
import sys
import threading
#import tqdm
import os
import time

BUFFER_SIZE = 65536
SEPARATOR = "<SEPARATOR>"

#ip and port numbers
l_ip = '127.0.0.1'   #local ip
ip = '127.0.0.1'     #dest ip

udp_l_port = 50002       #listening port
udp_s_port = 50003       #source port for sender
udp_d_port = 50004       #destination port for sender

#tcp addresses
tcp_s_adr = (ip, 50011) #tcp local server address
tcp_c_adr = (ip, 50012) #tcp local client address

p1_adr = (ip, 50013)    #tcp peer 1 server address 

#Tokens
token = '1'
p1 = 2

        
def tcp_server(SEPARATOR, BUFFER_SIZE, tcp_s_adr ):
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(tcp_s_adr)
    server.listen(10)
    
    print(f"[*] Listening as {tcp_s_adr}")
    client_socket, address = server.accept()
    print(f"[+] {address} is connected.")
    
    """
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
    client_socket.close()
    """
    server.close()
    return
    
# function opens a socket and is always listening, ready to receive messages
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((l_ip, udp_l_port))
    print ('listening\n')
    
    while True:
        data = sock.recv(1024).decode('utf-8')
        if (data == '2'):
            print('\rpeer: {} connected\n> '.format(data.decode()), end='')
            #TCP Server thread
            receiver = threading.Thread(target= tcp_server, args=(SEPARATOR, BUFFER_SIZE, tcp_s_adr))
            receiver.start
        else:
            print ("Unkown peer, connection blocked\n")
            
#starts a new thread that runs the listening function
listener = threading.Thread(target=listen, daemon=True);
listener.start()




#reads in input and sends to peer
def main():
    time.sleep(0.2)
    cmd = input('Enter you command: \n')
    if (cmd != 'send' and cmd != 'Send'):
         print('Command not recognized\n')     
    else:
         peer = input('Enter peer token number:\n')
    
    if(peer != '2'):
        print ('Peer unkown\n')
    else:
        file = input('Enter filenumber:\n')
        
    if(file != '1'):
        print('File not found\n')
    else:
        #opens the sending socket 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((l_ip, udp_s_port))
        sock.sendto(token.encode(), (ip, udp_d_port))
        
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((p1_adr))
        msg = ('hello friend').encode('utf-8')
        s.send(msg)
        s.close()
if __name__ == "__main__":
    main()      
    
    
    