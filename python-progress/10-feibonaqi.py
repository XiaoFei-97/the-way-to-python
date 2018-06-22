#菲波纳契数列

def createNum():
	print("----start---")
	a,b = 0,1
	print("-----1-----")
	for i in range(5):
		#print(b) #fib函数变成generator，只需要把print(b)改为yield b就可以了
		print("----2-----")
		yield b #加了yield就成了生成器
		print("------3-----")
		a,b = b,a+b
	print("-----stop----")

a = createNum()

#for num in a:
#	print(a) #print自动检测异常并停止,但是next()就要用try

#注意，这两种方法一样
#1.next(a)
#2.ret = a.__next__()


