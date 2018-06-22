from socket import *
from time import ctime

#1.创建套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)

#2.发送数据
sendData = input("请输入您要发送的消息：")
sendAddr = ("192.168.155.1",8080)
udpsocket.sendto(sendData.encode("gb2312"),sendAddr)

#3.接收数据
recvData = udpsocket.recvfrom(1024)
#如果要显示当前时间，注意要导入time模块的ctime，然后ctime(),注意这个括号
print("[%s]%s:%s"%(ctime(),recvData[1],recvData[0].decode("gb2312")))

#3.关闭套接字
udpsocket.close()
