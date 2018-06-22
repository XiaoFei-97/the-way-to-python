#线程，大大缩短运行时间

import time
from threading import Thread

#1.如果是多线程执行的都是同一个函数的化，各自之间不会有影响，各是各的
def test():
	print("---昨晚喝多了，下次少喝点")
	time.sleep(1)

if __name__ == "__main__":
	for i in range (5):
		t = Thread(target=test)
		t.start()
