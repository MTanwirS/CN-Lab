import socket as skt
import sys

serverport = 12000
serverhost = "192.168.1.101"
try:
    serverSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
except skt.error :
    print ('error creating socket')

try :
    serverSocket.bind((serverhost, serverport))
except skt.error:
    print ('error binding')

print ("The server is receiving")
while 1:
    message , clientAddress = serverSocket.recvfrom(2048)
    file=open(message ,"r")
    reply = file.read(2048)
    serverSocket.sendto(bytes(reply,"utf-8"),clientAddress)
    print("sent to client",reply)
file.close()