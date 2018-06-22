class Person(object):
	"""人的类"""
	def __init__(self,name):
		super(Person,self).__init__()
		self.name = name
	def anzhuang_zidan(self,zidan_temp,danjia_temp):
		"""把子弹装到弹夹中"""
		#弹夹.保存子弹(子弹)
		danjia_temp.baocun_zidan(zidan_temp)
	def anzhuang_danjia(self,gun_temp,danjia_temp):
		"""把弹夹保存到枪中"""
		gun_temp.baocun_danjia(danjia_temp)	

class Gun(object):
	"""枪的类"""
	def __init__(self,name):
		super(Gun,self).__init__()
		self.name = name #用来记录枪的类型
		self.danjia = None #用来记录所有弹夹的引用
	def baocun_danjia(danjia_temp):
		self.danjia = danjia_temp	
	
class Danjia(object):
	"""弹夹的类"""
	def __init__(self,max_num):
		super(Danjia,self).__init__()
		self.max_num = max_num #用来录弹夹的容量
		self.zidan_list = [] #用来记录所有子弹的引用
	def baocun_zidan(zidan_temp):
		"""将这颗子弹保存到弹夹"""
		self.zidan_list.append(zidan_temp)
	
		
	
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

	#3.创建子弹对象,20表示伤害
	zidan = Zidan(20)

	#4.创建弹夹对象,一个弹夹最多装30发
	danjia = Danjia(30)

	#5.创建枪的对象
	ak47 = Gun("AK47")

	#6.老蒋把子弹装到弹夹中
	laojiang.anzhuang_zidan(zidan,danjia)

	#7.把弹夹装到枪中
	#枪.安装（弹夹）
	laojiang.anzhuang_danjia(gun_temp,danjia_temp)

	#8.老蒋拿起枪

	#9.老蒋开枪杀敌人
if __name__="__main__":
	main()
