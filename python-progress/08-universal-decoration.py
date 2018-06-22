#----------通用装饰器------------

def w1(func):
	print("-----正在装饰-----")
	def inner(*args,**kwargs):
		print("---正在验证权限---")
		print("----记录日志----")
		ret = func(*args,**kwargs) #保存返回来的haha
		return ret #把haha返回到17行的调用
	return inner

#return
@w1 #就等于已经把f1函数体指向了w1的闭包,等价于f1 = w1(f1)	
def f1():
	print("----f1----")
	return "haha"

#没有参数，没有返回值
@w1
def f2():
	print("----f2-----")

#不定参数
@w1
def f3(a):
	print("-----f3-%d"%a)

ret = f1()
print(ret)

f2()
f3(4)
