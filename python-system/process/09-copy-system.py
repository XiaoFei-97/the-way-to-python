from multiprocessing import Pool,Manager
import os

def copyFileTask(name,olderFolderName,newFolderName):
	"完成copy一个文件的功能"
	fr = open(olderFolderName+"/"+name)
	fx = open(newFolderName+"/"+name,"w")
	
	content = fr.read()
	fw.write(content)

	fr.close()
	fw.close()
	queue.put(name)
def main():
	#0.获取用户需要copy的名字
	oldFolderName = input("请输入文件夹的名字:")

	#1.创建一个文件夹
	newFolderName = oldFolderName + "-附件"
	#print(newFolderName)
	os.mkdir(newFolderName)

	#2.获取old文件夹中的所有的文件名字
	fileName = os.listdir(oldFolderName)
	#print(fileName)

	#3.使用多进程的方式copy原文加中的所有文件到新的文件夹
	pool = Pool(5)
	queue = Manager.Queue()

	for name in fileName:
		pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName))

	num = 0
	allNum = len(fileName)
	while num<allNum:
		queue.get()
		num += 1
		copyRate = num/allNum
		print("\rcopy的进度是:%s.2f%"%(copyRate*100),end="")
	print("已完成")


	pool.close()
	pool.join()

if __name__ == "__main__":
	main()
