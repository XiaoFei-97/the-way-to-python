class Dog(object):
	def __init__(self):
		print("----init方法------")
	def __del__(self):
		print("----del方法-----")
	def __new__(cls):
		print("-----new方法-----")
		return object.__new__(cls)
	def __str__(self):
		print("-----str方法----")
		return "对象描述的信息"

#相当于要做3件事：
#1.调用__new__方法来创建爱呢对象，然后找了一个变量来接收__new__的返回值，这个返回值表示创建出来的对象的引用
#2.__init__(刚刚创建出来的对象的引用)
#3.返回对象的引用
xtq = Dog()
