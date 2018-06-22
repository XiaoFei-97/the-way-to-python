class Animal:
	def eat(self):
		print("---吃-----")
	def sleep(self):
		print("----睡----")


class Dog(Animal):
	#def bark(self):
		#print("----叫-----")
dog = Dog()
dog.eat()
#a = Animal()
#a.eat()
