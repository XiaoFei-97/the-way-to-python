from socket import *
import struct

sendData = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)

udpsocket = socket(AF_INET,SOCK_DGRAM)

udpsocket.sendto(sendData, ("192.168.43.206",69))

udpsocket.close()

