from socket import *

udpsocket = socket(AF_INET,SOCK_DGRAM)


#在python2中
udpsocket.sendto("haha",("192.168.119.115",8080))
#在python3中
udpsocket.sendto(b"haha",("192.168.119.115",8080))
