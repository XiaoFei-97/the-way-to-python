#_*_ coding:utf-8 _*_
#可以知道在进程与进程之间，他们是相互不影响的
#在子进程中对全局变量发生了改变，但是在父进程中丝毫不知道
import os
import time

g_num = 100
ret = os.fork()
if ret == 0:
	print("----process-1------")
	g_num += 1
	print("progress-1 g_num=%d--"%g_num)
else:
	time.sleep(3)
	print("-----progress-2-----")
	print("progress-2 g_num=%d--"%g_num)
