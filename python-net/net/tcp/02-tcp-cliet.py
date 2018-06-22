#tcp客户端的流程
#1.创建套接字
#2.连接connect服务器
#3.发送或接受数据
#4.关闭套接字

from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.43.206",8080))

clientSocket.send("haha".encode("gb2312"))
#注意：
#1.tcp客户端已经连接好了服务器，所以在以后的数据发送中，不需要填写对方的ip和port-->打电话
#2.udp在发送数据的时候，因为没有之前的连接，所以在需要在每次的连接中都要填写接收方的ip和port-->写信

recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData.decode("gb2312"))

clientSocket.close()
