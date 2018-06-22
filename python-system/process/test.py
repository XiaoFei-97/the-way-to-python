from multiprocessing import Process
import os

def test():
	while True:
		print("----1----%d"%os.getpid())
p = Process(target=test)
p.start()
p.join()
