#跨平台的操作，fork只在linux下才有效，所以平时应该使用process,它是一个类

from multiprocessing import Process
import time
import os

def test():
	#这是子进程
	while True:
		print("---test---")
		print("子进程的id=%d"%os.getpid())
		time.sleep(1)

P = Process(target=test)
P.start()  #让这个进程开始执行test函数里的代码
P.join() #堵塞，如果子进程没结束完，主进程就被堵塞

#主进程继续往下走
while True:
	print("---main---")
	time.sleep(1)
