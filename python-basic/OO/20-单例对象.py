class Dog(object):

	#区别是第一次调用__new__还是已经调用
	#类对象,私有属性
	__instance = None

	def __new__(cls):

		#如果没有创建
		if cls.__instance == None:
			#找个东西把这个对象存起来
			cls.__instance == object.__new__(cls) 
			return cls.__instance 
		else:
			return cls.__instance
			
		
a = Dog()
print(id(a))
b = Dog()
print(id(b))
			
