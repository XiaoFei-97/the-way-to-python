#多态
class Dog(object):
	def print_self(self):
		print("大家好，我是xxxxx，希望大家以后多多关照...")
class Xiaotq(Dog):
	def print_self(self):
		print("hello everybody")

#此处的temp并不知道是什么，只有在执行的时候才知道这个temp是谁，这就是多态
def introduce(temp):
	temp.print_self()	

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)


