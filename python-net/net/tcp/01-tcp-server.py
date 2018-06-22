#tcp的服务器流程
#1.创建一个套接字serverSocket
#2.bind绑定ip和port
#3.listen使套接字变为被动连接
#4.accept等待客户端的连接（clientsocket和clientInfo）
#5.recv/send接受发送数据
#6.关闭服务器套接字和客户端套接字

from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("",8899))

serverSocket.listen(5)

#clietSocket表示这个新的服务器端
#clientInfo表示这个新的服务器的ip以及port
clientSocket,clientInfo = serverSocket.accept()
sendData = "thank you!"
clientSocket.send(sendData.encode("gb2312"))

recvData = clientSocket.recv(1024)

print("%s:%s"%(str(clientInfo),recvData.decode("gb2312")))

clientSocket.close()
serverSocket.close()
