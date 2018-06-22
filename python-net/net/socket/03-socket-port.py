from socket import *
from time import ctime

#1.创建套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)

#2.绑定端口
bindAddr = ("",15462)
udpsocket.bind(bindAddr)
print("bindsuccess")

#3.接收数据
while True:
    print("--1--")
    recvData = udpsocket.recvfrom(1024)
    print(recvData)
    print("----1----")
    print("[%s]%s:%s"%(ctime(),recvData[1],recvData[0].decode("gb2312")))

#4.关闭套接字
udpsocket.close()
