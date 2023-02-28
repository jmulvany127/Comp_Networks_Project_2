import socket

def get_ip(host):
    ip_ad =socket.gethostbyname(host)
    return ip_ad