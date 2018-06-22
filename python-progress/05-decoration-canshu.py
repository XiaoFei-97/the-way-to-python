#----------有参数装饰器------------

def w1(func):
	print("-----正在装饰-----")
	#如果a,b没有定义，那么会导致19行的调用失败
	def inner(a,b):
		print("---正在验证权限---")
		if True:
			func(a,b) #如果没有把a,b当作实参进行传递，那么会导致调用15行的函数失败
		else:
			print("没有权限")
	return inner

@w1 #就等于已经把f1函数体指向了w1的闭包,等价于f1 = w1(f1)	
def f1(a,b):
	print("----f1-a=%d,b=%d"%(a,b))
	

f1(11,22)
