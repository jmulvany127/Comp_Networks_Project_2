import socket
import sys
import threading

l_ip = '127.0.0.1'
ip = '127.0.0.1'
l_port = 50002
s_port = 50001
d_port = 50004


# listen for
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', l_port))
    print ('listening')
    
    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()


# send messages
# equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 54444))

while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (ip, dport))