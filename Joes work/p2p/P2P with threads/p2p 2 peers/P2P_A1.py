
import socket
import sys
import threading
# import tqdm
import os
import time

BUFFER_SIZE = 65536
SEPARATOR = "<SEPARATOR>"

#ip and port numbers
l_ip = '127.0.0.1'   #local ip
ip = '127.0.0.1'     #dest ip

udp_l_port = 50004       #listening port
udp_s_port = 50001       #source port for sender
udp_d_port = 50002       #destination port for sender

#tcp addresses
tcp_s_adr = (ip, 50013) #tcp local server address
tcp_c_adr = (ip, 50014) #tcp local client address

p1_adr = (ip, 50011)    #tcp peer 1 server address 

#Tokens
token = '2' 
p1 = '1'

             
#starts a new thread that runs the listening function
def server():
    print('entered tcp server thread\n')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(tcp_s_adr)
    server.listen(10)
    
    print(f"[*] Listening as {tcp_s_adr}")
    client_socket, address = server.accept()
    print(f"[+] {address} is connected.")
    recieved = client_socket.recv(1024)
    recieved = recieved.decode('utf-8')
    print((recieved))

    server.close()
    
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((l_ip, udp_l_port))
    print ('listening')
    
    while True:
        data = sock.recv(1024).decode('utf-8')
        if (data == p1):
            print(f'peer: {data} connected\n')
            #TCP Server thread
            TCPserver = threading.Thread(target=server, daemon=True)
            TCPserver.start()

            print('server threadstarted\n')
            time.sleep(100)
        else:
            print ("Unkown peer, connection blocked\n")


#reads in input and sends to peer
def main():
    listener = threading.Thread(target=listen, daemon=True)
    listener.start()
    
    time.sleep(0.2)
    while True:
        cmd = input('Enter you command: \n')
        if (cmd != 'send' and cmd != 'Send'):
            print('Command not recognized\n')     
        else:
            peer = input('Enter peer token number:\n')
        
        if(peer != '1'):
            print ('Peer unkown\n')
        else:
            file = input('Enter filenumber:\n')
            
        if(file != '1'):
            print('File not found\n')
        else:
            #opens the udp sending socket 
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((l_ip, udp_s_port))
            sock.sendto(token.encode(), (ip, udp_d_port))
            sock.close()
            
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((p1_adr))
            msg = ('hello friend').encode('utf-8')
            s.send(msg)
            s.close()
        
   
        
if __name__ == "__main__":
    main()    