#from threading import Thread
import time
import threading

class My_thread(threading.Thread):
	def run(self):
		for i in range(3):
			time.sleep(1)
			msg = "I'm"+self.name+"@"+str(i)
			print(msg)
if __name__ == "__main__":
	for i in range(5):
		t = My_thread()
		t.start()
