from threading import Thread
from socket import *

#1.收数据，然后打印
def recvData():
	while True:
		recvInfo = udpsocket.recvfrom(1024)
		print(">>%s:%s"%(str(recvINfo[1]),recvINfo[0]))

#2.检测键盘，发数据
def sendData():
	while True:
		sendInfo = input("<<")
		udpsocket.sendto(sendInfo.encode("gb2312"),(destIP,destPort))

#创建全局的udpsocket
udpsocket = None
destIP = ""
destPort = 0


def main():	
	global udpsocket
	global destIP
	global destPort

	destIP = input("对方的IP:")
	destPort = input("对方的Port:")
	udpsocket = socket(AF_INET,SOCK_DGRAM)
	udpsocket.bind(("",4567))

	tr = Thread(target=recvData)
	ts = Thread(target=sendData)
	
	ts.start()
	tr.start()

	ts.join()
	tr.join()

if __name__ == "__main__":
	main()
