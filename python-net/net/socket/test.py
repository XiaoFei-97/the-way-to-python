from threading import Thread
from socket import *

def recvData():
    while True:
        recvInfo = udpsocket.recvfrom(1024)
        print(">>%s:%s"(str(recvInfo[1]), recvInfo[0].decode("gb2312")))

def sendData():
    while True:
        sendInfo = input("<<")
        udpsocket.sendto(sendInfo.encode("gb2312"), (destIP,destPort))

udpsocket = None
destIP = ""
destPort = 0

def main():
    
    global udpsocket
    global destIP
    global destPort

    destIP = input("对方的ip:")
    destPort = int(input("对方的Port:")) 

    udpsocket = socket(AF_INET,SOCK_DGRAM)
    udpsocket.bind(("",4567))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()
    
    tr.join()
    ts.join()

if __name__ == "__main__":
    main()
