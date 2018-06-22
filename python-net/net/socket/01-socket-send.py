from socket import *

#1.创建套接字
socket = socket(AF_INET,SOCK_DGRAM) 

#2.发送数据python2

sendData = "我爱你"
sendAddr = ("10.91.30.205",8080)
socket.sendto(sendData.encode("gb2312"),sendAddr)

#3.关闭套接字
socket.close()
