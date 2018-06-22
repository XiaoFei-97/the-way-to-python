from socket import *
from threading import Thread
from time import ctime

def recvData():
    while True:
        recvInfo = udpsocket.recvfrom(1024)
       # print(">>[%s]%s:%s"%(ctime,recvInfo[1],recvInfo[0].decode("gb2312")))
        print(">>[%s]%s:%s"%(ctime(), str(recvInfo[1]), recvInfo[0]))

def sendData():
    while True:
        sendInfo = input("<<")
        udpsocket.sendto(sendInfo.encode("gb2312"), (sendIP,sendPort))

udpsocket = None
sendIP = "" 
sendPort = 0 
    
def main():
    global udpsocket
    global sendIP
    global sendPort

    #获取用户输入的地址和信息
    sendIP = input("请输入您要发送的IP地址:")
    sendPort = int(input("请输入您要发送的端口号:"))
    #1.创建套接字
    udpsocket = socket(AF_INET,SOCK_DGRAM)
    udpsocket.bind(("",4567))

    #2.发数据
    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()
    #3.收数据
    #tr = Thread(target=recvData)
    #tr.start()
    #tr.join()
    #4.关闭套接字
    #udpsocket.close()

if __name__ =="__main__":
    main()
