#----------装饰器------------

def w1(func):
	#这句话在f1调用之前，已经进行装饰了
	print("-----正在装饰-----")
	def inner():
		print("---正在验证权限---")
		if True:
			func()
		else:
			print("没有权限")
	return inner

@w1 #就等于已经把f1函数体指向了w1的闭包,等价于f1 = w1(f1)	
def f1():
	print("---f1---")

#innerFunc就等于指向了inner()
#innerFunc = w1(f1)
#innerFunc()

#此时f1不再指向第八行函数体，而是指向了w1里面的闭包
#f1 = w1(f1)
f1()
