#多继承
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

dog = Dog()
dog.eat()

xiaotq = xiaotq()
xiaotq.fly()
#a = Animal()
#a.eat()
