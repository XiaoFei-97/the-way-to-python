#----------带有参数的装饰器------------

def func_arg(arg):
	def w1(func):
		print("---记录日志---")
		def inner(*args,**kwargs):
			func(*args,**kwargs) #保存返回来的haha
		return inner
	return w1

#先执行func_arg("heihei")函数，这个函数return的结果是
#2.@w1
#3.使用@w1对f1进行装饰

#带有参数的装饰器，能够起到在运行时，有不同的功能
@func_arg("heihei") 
def f1():
	print("----f1----")


f1()

