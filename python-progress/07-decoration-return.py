#----------return函数的装饰器------------

def w1(func):
	print("-----正在装饰-----")
	def inner():
		print("---正在验证权限---")
		ret = func() #保存返回来的haha
		return ret #把haha返回到17行的调用
	return inner

@w1 #就等于已经把f1函数体指向了w1的闭包,等价于f1 = w1(f1)	
def f1():
	print("----f1----")
	return "haha"

ret = f1()
print(ret)
