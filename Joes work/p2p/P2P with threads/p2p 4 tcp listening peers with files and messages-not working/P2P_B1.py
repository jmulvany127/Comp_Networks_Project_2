
import socket
import sys
import threading
import tqdm
import os
import os.path
import time

BUFFER_SIZE = 65536
SEPARATOR = "<SEPARATOR>"

#file location and size
filepath = 'C:\\Users\\jsmul\\Desktop\\College Year 3\\Semester 2\\3D3 Computer Networks\\Project 2\\project 2 repo\\Joes work\\p2p\\P2P with threads\\p2p 4 peers with files\\DataBase_B\\DATABASE.txt'
filesize = os.path.getsize(filepath)

#Tokens to be replaced
token = '2' 
p1 = '3'
p2 = '4'
p3 = '1'

#number of connections
connections = 0

#ip and port numbers
l_ip = '127.0.0.1'   #local ip
ip = '127.0.0.1'     #dest ip

udp_l_port = (50000 + int(token))     #listening port
udp_s_port = (50100 +  int(token))     #source port for sender

tcp_s_port = (50000 + 10*int(token) )  #tcp local server address
tcp_s_adr = (ip, tcp_s_port) #tcp local server address

p_port = 50000 #base port for new peers
p_addr = (ip, p_port) #base address for new peers

rcved = False #boolean to indicate whether or not peer TCP Connection recievd

             
#function opened in new thread
#function sets up a tcp server socket for receiving messages from peers
def msg_server():
    #print('entered tcp server thread\n') #debug
    
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
    
    #decrements the connections when socket closed
    global connections 
    connections = connections - 1

#function opened in new thread
#function sets up a tcp server socket for receiving messages from peers
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
    #progress bar
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    #while loop reads in bytes, saves bytes and then overwrites local file with these bytes 
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f = open(filepath, "wb")
        f.write(bytes_read)
        progress.update(len(bytes_read))
    client_socket.close()
    file_server.close()
    
    #decrements the connections when socket closed
    global connections 
    connections = connections - 1

#function opened in new thread
#function sets up an always on udp server socket for receiving messages from peers  
def listen():
    
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((l_ip, udp_l_port))
    sock.listen(10)
    print ('listening')

    client_socket, address = sock.accept()
    print(f"[+] {address} is attempting to connect")

    while True:
        while True:
            #blocking call reads in and decodes data 
            data = client_socket.recv(1024).decode('utf-8')
            print (f"received data {data}") #debug
            if (data== ''):
                break
            #if peer is on peer list then handle new connection
            elif ((data == p1 or data ==  p2 or data == p3 or data == token ) ):
                print(f'peer: {data} connected\n')
                #marker for file or text data
                marker = client_socket.recv(1024).decode('utf-8')
                #increments connection count
                global connections 
                connections = connections + 1
                
                #update tcp_s port and address, this is where our local tcp server socket will be binded to 
                global tcp_s_port
                tcp_s_port = tcp_s_port + connections
                global tcp_s_adr
                tcp_s_adr = (ip, tcp_s_port)
                
                #update the port number of the peers udp listening port 
                udp_d_port = 50000 + int(data)
                #print(udp_d_port)
                
                #open TCP Server thread
                if (marker == 'f'):
                    f_server = threading.Thread(target=file_server, daemon=True)
                    f_server.start()
                elif (marker == 't'):
                    m_server = threading.Thread(target=msg_server, daemon=True)
                    m_server.start()
                

                #send our local tcp server port to the peer listening tcp port 
                send_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                send_sock.connect((ip,udp_d_port ))
                send_sock.send((str(tcp_s_port)).encode())
                send_sock.close()
                print(f"server address{tcp_s_adr}sent to udp port{udp_d_port}")
                
            #numbers in this range are receved tcp port numbers
            elif (int(data) >= 50000 and int(data) <=60000):
                #update the peer port 
                global p_port
                p_port = int(data)
                
                global p_addr
                p_addr = (ip, p_port)
                print(f"new peer address received {p_addr}") #debug
                global rcved
                
                #upate the received variable
                rcved = True 
                
            else:
                print ("Unkown peer, connection blocked\n")

#function to send typed messages to peer
def send_message(ip, udp_d_port):
            #opens the tcp pinging socket 
            send_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            send_sock.connect((ip,udp_d_port ))
            send_sock.send(token.encode())

            time.sleep(0.1)
            marker = 't'
            send_sock.send(marker.encode())
            send_sock.close()
           
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
                    msg = input('Input peer message: \n ').encode('utf-8')
                    s.send(msg)
                    s.close()
                    
                    p_port = 50000
                    break 
        
#function to send files to peer        
def send_file(ip, udp_d_port):
     
     send_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     send_sock.connect((ip,udp_d_port ))
     send_sock.send(token.encode())

     time.sleep(0.1)
     marker = 'f'
     send_sock.send(marker.encode())
     send_sock.close()
     #opens the udp sending socket 
     
     global p_port 
     global rcved
     
     time.sleep(0.2)
     #waits for peer to send back the tcp port number, received will be true here
     print(f"waiting for the peer socket address")
     while True:
        if (rcved == True):
            #open tcp client and sends filename and size to peer tcp peer 
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((p_addr))
            s.send(f"{filepath}{SEPARATOR}{filesize}".encode())
            
            #prints local progress message
            filename = os.path.basename(filepath)
            progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
            
            #reads file in byte wise and sends final packet to peer
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
        peer = input('Enter peer token number:\n')
        
        if(peer != p1 and peer != p2 and peer != p3):
            print ('Peer unkown\n')
        else:
            udp_d_port = 50000 + int(peer)
            cmd = input('Enter command, msg or file: \n')
        
        if (cmd == 'msg'):
            send_message(ip, udp_d_port)
        elif(cmd == 'file'):
            send_file(ip, udp_d_port)
        
if __name__ == "__main__":
    main()      
