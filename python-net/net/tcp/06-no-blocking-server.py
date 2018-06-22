from socket import *

#1.创建套接字
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#2.绑定本地端口
serverSocket.bind(("",7788))

#3.设置非堵塞模式
serverSocket.setblocking(False)

#4.设置最大连接数
serverSocket.listen(10)

g_clientInfo = []
while True:
    try:
        #由主动转为被动
        clientSocket,clientAddr = serverSocket.accept()
    except:
        pass
    else:
        #打印出客户端套接字信息
        print("一个新的客户端到来[%s]"%str(clientAddr))
        clientSocket.setblocking(False)
        g_clientInfo.append((clientSocket,clientAddr))

    dellist = []
    #遍历出非堵塞情况下的所有连接的信息
    for clientSocket,clientAddr in g_clientInfo:
         try:
             recvData = clientSocket.recv(1024)
         except:
             pass
         else:
             print("----1----")
             if len(recvData) > 0:
                 print("[%s]%s"%(str(clientAddr),recvData))
             else:
                 print("----2----")
                 clientSocket.close()
                 dellist.append((clientSocket,clientAddr))
                 print("客户端%s已下线"%str(clientAddr))
                 for dellist in g_clientInfo:
                     g_clientInfo.remove(dellist)



