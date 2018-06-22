from multiprocessing import Process,Queue
import os,time,random

#写数据进程代码
def write(q):
	for value in['A','B','C']:
		print("put %s to queue"%value)
		q.put(value)
		time.sleep(random.random())

#读数据执行代码
def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print("get %s from queue"%value)
		else:
			break

if __name__ == "__main__":
	#父进程创建Queue,并传给各个子进程
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	#启动子进程写入
	pw.start()
	#等待子进程结束
	pw.join()
	
	#启动子进程读取
	pr.start()
	#等待子进程结束
	pr.join()
	print('')
	print("所有数据都写完且读完")

