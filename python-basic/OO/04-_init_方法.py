class Cat:
	#属性
	#方法

	#初始化对象，python会自动调用init方法,称之为魔法方法
	def __init__(self,new_name,new_age):
		self.name = new_name
		self.age = new_age
	def eat(self):
		print("猫在吃鱼....")

	def drink(self):
		print("猫正在喝可乐....")
	def introduce(self):
		#print(tom.name)
		#这样的话就变成每个对象介绍它自己
		print(self.name)

#创建一个对象
tom = Cat("tom",40)
tom.drink()

lanmao = Cat("lanmao",10)
lanmao.eat()
#这里的问题在于lanmao.introduce()没有介绍自己
#这里的实参不能传递参数
lanmao.introduce()
