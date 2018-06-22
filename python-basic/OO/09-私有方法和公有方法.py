class Dog:
	#私有方法
	def __send_msg(self):
		print("------正在发送短信--------")
	#公有方法
	def send_msg(self,money):
		if money>100:
			self.__send_msg()
		else:
			print("余额不足")

dog = Dog()
#dog.__send_msg()
dog.send_msg(100)
