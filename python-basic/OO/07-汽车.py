#给汽车加油的行驶问题
#1L油走100km

class Car:
	#定义了这个类的所有方法
	def __init__(self,new_name):
		self.name = new_name 
		self.oil = 100
		self.color = "白色"
		self.distance = 0

	def __str__(self):
		return "%s的%s还有%s的油，已经跑了%skm"%(self.color,self.name,self.oil,self.distance)	

	def move(self):
		if self.oil >=20 and self.oil <= 100:
			self.oil -= 20
			self.distance += 100
		elif self.oil < 20:
			self.distance += self.oil
			self.oil = 0
		elif self.oil <= 0:
			print("没有油了，不跑了...")
	def add_oil(self,volume):
		self.oil += volume	
		if self.oil > 100:
			self.oil = 100
		print(self.oil)

BWM = Car("BWM")

#打印功能序号
print("  赛车游戏 V2.0")
print("*"*50)
print("   1.加油")
print("   2.开车")
print("*"*50)

while True:
	num = int(input("输入功能序号："))
	if num == 1:
		BWM.add_oil(10)
		print(BWM)
	elif num == 2:
		BWM.move()
		print(BWM) 
	else: 
		print("你的输入有误")
