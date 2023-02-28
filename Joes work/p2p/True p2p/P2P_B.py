import socket
import sys
import threading

#ip and port numbers
l_ip = '127.0.0.1'   #local ip
ip = '127.0.0.1'     #dest ip

l_port = 50002       #listening port
s_port = 50003       #source port for sender
d_port = 50004       #destination port for sender


# function opens a socket and is always listening, ready to receive messages
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((l_ip, l_port))
    print ('listening')
    
    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')
        
#starts a new thread that runs the listening function
listener = threading.Thread(target=listen, daemon=True);
listener.start()

#opens the sending socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((l_ip, s_port))

#reads in input and sends to peer
print ('talk to your friends!')
while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (ip, d_port))