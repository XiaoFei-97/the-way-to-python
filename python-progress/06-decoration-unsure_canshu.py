#----------不定长参数装饰器------------

def w1(func):
	print("-----正在装饰-----")
	#如果a,b没有定义，那么会导致19行的调用失败
	def inner(*args,**kwargs):
		print("---正在验证权限---")
		if True:
			func(*args,**kwargs) #如果没有把a,b当作实参进行传递，那么会导致调用15行的函数失败
		else:
			print("没有权限")
	return inner

@w1 #就等于已经把f1函数体指向了w1的闭包,等价于f1 = w1(f1)	
def f1(a,b,c):
	print("----f1-a=%d,b=%d,c=%d"%(a,b,c))
@w1	
def f2(a,b,c,d):
	print("----f1-a=%d,b=%d,c=%d,d=%d"%(a,b,c,d))

f1(11,22,33)
f2(11,22,33,44)
