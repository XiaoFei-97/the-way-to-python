#在python3中接收数据并解码

from socket import *

socket = socket(AF_INET,SOCK_DGRAN)

socket.bind("",7789)
sendData = socket.recvfrom(1024)

#这里是把接收到的数据内容给content，把发送方信息给destINfo
content,destInfo = recvData

print("content is %s"%content)
print("content is %s"%content.decode("gb2312"))
