
import socket
import sys
import threading
import tqdm
import os
import time


BUFFER_SIZE = 65536
SEPARATOR = "<SEPARATOR>"

#file location and name
filedirectiory=("C:\\Users\\jsmul\Desktop\\College Year 3\\Semester 2\\3D3 Computer Networks\\Project 2\\project 2 repo\\Server Connect")
filename = ("masterpiece.png")
filepath = ("C:\\Users\\jsmul\\Desktop\\College Year 3\\Semester 2\\3D3 Computer Networks\\Project 2\\project 2 repo\\Server Connect\\masterpiece.png")

filesize = os.path.getsize(filepath)



#Tokens
token = '1' 
p1 = '3'
p2 = '4'
p3 = '2'

#number of connections
connections = 0

#ip and port numbers
l_ip = '127.0.0.1'   #local ip
ip = '127.0.0.1'     #dest ip

udp_l_port = (50000 + int(token))     #listening port
udp_s_port = (50100 +  int(token))     #source port for sender

tcp_s_port = (50000 + 10*int(token) )  #tcp local server address
tcp_s_adr = (ip, tcp_s_port) #tcp local server address

p_port = 50000
p_addr = (ip, p_port)

rcved = False

             
#starts a new thread that runs the listening function
def msg_server():
    #print('entered tcp server thread\n')
    msg_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    msg_server.bind(tcp_s_adr)
    msg_server.listen(10)
    
    print(f"[*] Listening as {tcp_s_adr}")
    client_socket, address = msg_server.accept()
    print(f"[+] {address} is connected.")
    recieved = client_socket.recv(1024)
    recieved = recieved.decode('utf-8')
    print((recieved))

    msg_server.close()

def file_server():
    #print('entered tcp server thread\n')
    file_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_server.bind(tcp_s_adr)
    file_server.listen(10)
    
    print(f"[*] Listening as {tcp_s_adr}")
    client_socket, address = file_server.accept()
    print(f"[+] {address} is connected.")
    
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
    file_server.close()

    
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((l_ip, udp_l_port))
    print ('listening')
    
    while True:
        data = sock.recv(1024).decode('utf-8')
        #print ((data))
        if ((data == p1 or data ==  p2 or data == p3 or data == token ) ):
            print(f'peer: {data} connected\n')
            
            global connections 
            connections = connections + 1

            global tcp_s_port
            tcp_s_port = tcp_s_port + connections
            #print(tcp_s_port)
            
            global tcp_s_adr
            tcp_s_adr = (ip, tcp_s_port)
            
            
            udp_d_port = 50000 + int(data)
            #print(udp_d_port)
            
            #TCP Server thread
            TCPserver = threading.Thread(target=file_server, daemon=True)
            TCPserver.start()
            

            send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            send_sock.bind((l_ip, udp_s_port))
            send_sock.sendto((str(tcp_s_port)).encode(), (ip,udp_d_port ))
            send_sock.close()
            print(f"server address{tcp_s_adr}sent to udp port{udp_d_port}")
            

        elif (int(data) >= 50000 and int(data) <=60000):
            global p_port
            p_port = int(data)
            
            global p_addr
            p_addr = (ip, p_port)
            #print(f"new peer address received {p_addr}")
            global rcved
            rcved = True 
            
        else:
            print ("Unkown peer, connection blocked\n")

<<<<<<< Updated upstream
def send_message(ip, udp_d_port):
=======

#reads in input from user
def main():
    listener = threading.Thread(target=listen, daemon=True)
    listener.start()
    
    time.sleep(0.2)
    while True:
       
       print("Enter peer number/s which you want to connect to, if you want to connect to more than one ,add a comma between the numbers")
       numbers = input("")
       splitting(numbers)
       
       
       
       """
        cmd = input('Enter you command: \n')
        if (cmd != 'send' and cmd != 'Send'):
            print('Command not recognized\n')     
        else:
            peer = input('Enter peer token number:\n')
        
        if(peer != p1 and peer != p2 and peer != p3 and peer != token):
            print ('Peer unkown\n')
        else:
            
            udp_d_port = 50000 + int(peer)
            file = input('Enter filenumber:\n')
            
        if(file != '1'):
            print('File not found\n')
        """
        else:
>>>>>>> Stashed changes
            #opens the udp sending socket 
            send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            send_sock.bind((l_ip, udp_s_port))
            send_sock.sendto(token.encode(), (ip, udp_d_port))
            send_sock.close()
           
            global p_port 
            global rcved
            
            time.sleep(0.2)
            #waits for peer to send back the tcp port number, received will be true here
            print(f"waiting for the peer socket address")
            while True:
                if (rcved == True):
                    #open tcp client and send message to peer tcp peer 
                    print (f"sending hello to {p_port}")
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.connect((p_addr))
                    msg = ('hello friend').encode('utf-8')
                    s.send(msg)
                    s.close()
                    
                    p_port = 50000
                    break 
        
def send_file(ip, udp_d_port):
     
     send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     send_sock.bind((l_ip, udp_s_port))
     send_sock.sendto(token.encode(), (ip, udp_d_port))
     send_sock.close()
     #opens the udp sending socket 
     
     global p_port 
     global rcved
     
     time.sleep(0.2)
     #waits for peer to send back the tcp port number, received will be true here
     print(f"waiting for the peer socket address")
     while True:
        if (rcved == True):
            #open tcp client and send message to peer tcp peer 
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((p_addr))
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
    
            p_port = 50000
            break 
    


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
        
        if(peer != p1 and peer != p2 and peer != p3 and peer != token):
            print ('Peer unkown\n')
        else:
            
            udp_d_port = 50000 + int(peer)
            file = input('Enter filenumber:\n')
            
        if(file != '1'):
            print('File not found\n')
        else:
            send_file(ip, udp_d_port)

   
        
if __name__ == "__main__":
    main()      