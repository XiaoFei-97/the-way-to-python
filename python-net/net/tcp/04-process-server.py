from socket import *
from multiprocessing import Process

def Dealwithclient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print("recvData=%s,destAddr=%s"%(recvData,destAddr))
        else:
            print("客户端已经关闭...")
            newSocket.close()
        
def main():
    #1.创建套接字
    tcpSocket = socket(AF_INET,SOCK_STREAM)
    tcpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
    #2.绑定端口信息
    localAddr = ("",2678)
    tcpSocket.bind(localAddr)
    #3.监听，主动转被动
    tcpSocket.listen(5)
    try:
        while True:
            print('-----主进程，，等待新客户端的到来------')
            #4.accept创建新的客户端套接字
            newSocket,destAddr = tcpSocket.accept()
            print('-----主进程，，接下来创建一个新的进程负责数据处理[%s]-----'%str(destAddr))
            #5.创建新的进程
            client = Process(target=Dealwithclient,args=[newSocket,destAddr]) 
            client.start()
            #因为已经给子进程copy了一份newSocket，所以这里可以关闭
            newSocket.close()
    finally:
        tcpSocket.close()

if __name__ == "__main__":
    main()
