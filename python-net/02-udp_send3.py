#在python3中的程序

from socket import *

udpsocket = socket(AF_INET,SOCK_DGRAM)

destIp = input("请输入目的ip:")
destPort = input("请输入目的port:")
sendData = input("请输入要发送的数据:")

#udpsocket.sendto(sendData.encode("utf-8"),(destIp,destPort))
#换成gb2321的编码
udpsocket.sendto(sendData.encode("gb2321"),(destIp,destPort))
