import socket as skt
import sys

servername = "192.168.1.101"
serverport = 12000
csocket = skt.socket(skt.AF_INET,skt.SOCK_DGRAM)
message = input("Enter file")
csocket.sendto(bytes(message,"utf-8"),(servername, serverport))
filecontents,serverAddress = clientSocket.recvfrom(2048)
print ('Server says:', filecontents)

clientSocket.close()