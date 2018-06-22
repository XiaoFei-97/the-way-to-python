class Cat:
	#属性
	#方法
	def eat(self):
		print("猫在吃鱼....")

	def drink(self):
		print("猫正在喝可乐....")
	def introduce(self):
		print(tom.name)
		

#创建一个对象
tom = Cat()

#属性
tom.name = "汤姆"
tom.age = "40"
#print(tom.name)

#调用tom指向的对象中的方法
tom.drink()
tom.eat()
tom.introduce()



lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 10
#这里的问题在于lanmao.introduce()没有介绍自己
lanmao.introduce()
