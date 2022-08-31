import sys
import socket
port = 65535
ip = "192.168.115.213"

try:
    for i in range(1,100):
        conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = conn.connect_ex((ip,i))
        if result == 0:
            print("port {} open".format(i))
        
except:
        print("error !!!")
        print("exiting the program")
        sys.exit()