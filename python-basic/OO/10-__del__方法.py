class Dog:
	#如果是对象的引用个数在程序结束之前被删除完，那么在最后一个删除对象的时候会触发调用del方法，但如果是没有删除完引用对象，那么就会在程序结束之后才会调用这个方法
	def __del__(self):
		print("------英雄over------")

dog1 = Dog()
dog2 = dog1

del dog1
#del dog2
print("=================")
