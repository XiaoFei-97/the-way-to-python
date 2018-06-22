class Car_Store(object):
	def car_oder(self,money):
		if money < 50000:
			return Car()
		if money >100000:
			return Car()

class Car(object):
	def move(self):
		print("车在移动...")
	def music(self):
		print("正在播放音乐...")
	def stop(self):
		print("车在停止...")

car_store = Car_Store()
QQ = car_store.car_oder(100000)
QQ.move()
QQ.stop()
QQ.music()

BenTian = car_store.car_oder(1000000000)
BenTian.move()
