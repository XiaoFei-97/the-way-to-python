from socket import *

countNum = input("请输入要链接的次数:")
for i in range(int(countNum)):
    tcpClient = socket(AF_INET,SOCK_STREAM)
    tcpClient.connect(("192.168.40.128",7788))
    print(i)
