import socket as skt
import sys

serverport = 12000
serverhost = "192.168.1.101"
try:
    serverSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
except skt.error,msg:
    print 'error creating socket'+ str(msg[0]) + msg[1]
    sys.exit()

try :
    serverSocket.bind((serverhost, serverport))
except skt.error,msg:
    print 'error binding'+ str(msg[0]) + msg[1]

print ("The server is receiving")
while 1:
    message,clientAddress = serverSocket.recvfrom(1024)
    reply = 'Received' + message
    file=open(sentence,"r")
    reply = reply + file.read(2048)
    serverSocket.sendto(bytes(reply,"utf-8"),clientAddress)
    print("sent to client",reply)
file.close()