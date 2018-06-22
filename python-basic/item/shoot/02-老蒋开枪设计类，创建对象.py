class Person(object):
	"""人的类"""
	def __init__(self,name):
		super(Person,self).__init__()
		self.name = name

class Gun(object):
	"""枪的类"""
	def __init__(self,name):
	super(Gun,self).__init__()
	self.name = name #用来记录枪的类型
	
class Danjia(object):
	"""弹夹的类"""
	def __init__(self,max_num):
		super(Gun,self).__init__()
		self.max_num = max_num #用来录弹夹的容量
	
class Zidan(object):
	"""子弹的类"""
	def __init__(self,shanghai):
		super(Zidan,self).__init__()
		self.shanghai = shanghai #用来记录子弹的杀伤力
def main():
	'''用来控制整个程序的流程'''
	pass
	
	#1.创建老蒋对象
	laojiang = Person("老蒋")

	#2.创建一个敌人

	#3.创建子弹对象
	zidan = Zidan(20)

	#4.创建弹夹对象
	danjia = Danjia(30)

	#5.创建枪的对象
	ak47 = Gun("AK47")

	#6.把子弹装到弹夹中

	#7.把弹夹装到枪中

	#8.老蒋拿起枪

	#9.老蒋开枪杀敌人
if __name__="__main__":
	main()
