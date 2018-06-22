from socket import *
from multiprocessing import Process

def clientDeal(clientSocket):
    while True:
        sendData = input("请输入信息：")
        clientSokcet.send(sendData.encode("gb2312"))
        recvData = clientSocket.recv(1024)
        if len(recvData) > 0:
            print(">>%s"%recvData.decode("gb2312"))
        else:
            break
    clientSocket.close()

#创建一个服务端套接字
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("",8080))
serverSocket.listen(5)

while True:
    clientSocket,clientSocket = serverSocket.accept()
    p = Process(target=clientDeal,args=(clientSocket,))
    p.start()

serverSocket.close()


