import socket 
import sys
import select
from time import time
from binascii import unhexlify
from binascii import b2a_base64


#this program allows you to create a socket between yourself and a 
#server running on a local network. Connect to a host (yourself in a 
#seperate terminal) running server.py to receive message


#IP and PORT variables should contain valid ip and port numbers for
#host on local network running server.py
IP = "192.168.0.101"
PORT = 8000

#time intervals between characters being received are mapped to binary 
ZERO = 0.025
ONE = 0.1



#create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server
server.connect((IP, PORT))

covert_bin = " "

#evaluates time between characters received and maps to 0 or 1
while True:
    t0 = time()
    data = server.recv(4096)
    t1 = time()
    delta = round(t1 - t0, 3)
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"
    if not data: break
    # prints the character and the time interval in which it was received
    # Allowing us to debug and adjust our binary mappings during the challenge as 
    # the server may be sending data in different time intervals than .1 and .025
    print("{}  {}".format(data, delta))

covert_bin = covert_bin[2:]


covert = ""
i = 0
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 8]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)

    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i += 8

print("Covert message: {}".format(covert.split("EOF")[0]))
