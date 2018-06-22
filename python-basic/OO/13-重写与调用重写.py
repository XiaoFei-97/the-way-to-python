#重写与调用重写
class Animal:
	#定义一个类叫动物
	def eat(self):
		print("---吃-----")
	def sleep(self):
		print("----睡----")


class Dog(Animal):
	#定义一个类叫狗
	def bark(self):
		print("----叫-----")
	
class xiaotq(Dog):
	#定义一个类叫啸天犬
	def fly(self):
		print("-----飞-----")
	
	#重写
	def bark(self):
		print("----旺旺叫-----")
		#第一种重调用方法
		#super().bark()
		#第二种重调用方法
		Dog.bark(self)

dog = Dog()
dog.eat()

xiaotq = xiaotq()
xiaotq.bark()
#a = Animal()
#a.eat()
