from socket import *
from time import sleep

#创建套接字
tcpServer = socket(AF_INET,SOCK_STREAM)
#绑定本地信息
addr = ("",7788)
tcpServer.bind(addr)

countNum = input("请输入最大连接数:")
#listen从主动转为被动
tcpServer.listen(int(countNum))
for i in range(10):
    print(i)
    sleep(1)
print("延时结束...")
while True:
    #如果有新的客户端来连接服务器，就产生一个新的套接字
    client,clientInfo = tcpServer.accept()
    print(clientInfo)
    sleep(1)
