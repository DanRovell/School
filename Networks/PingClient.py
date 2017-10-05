#Daniel Rovell
#Assignment 2

import time
from socket import *

for pings in range(10):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    x = "message"
    message = x.encode()
    addr = ("localhost", 12000)

    start = time.time()
    clientSocket.sendto(message, addr)
    try:
        data, server = clientSocket.recvfrom(1024)
        stop = time.time()
        elapsed = stop - start
        print ("Ping:" '%d ' ' %f' % (pings + 1, elapsed))
    except timeout:
        print ('Request timed out')
