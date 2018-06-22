#类属性和实例属性
class Tool(object):

	#属性,与self.name完全不是一个性质，称之为类属性
	num = 0

	#方法
	def __init__(self,new_name):
		#self.name称为实例属性
		self.name = new_name
		Tool.num += 1

tool1 = Tool("铁锹")
tool2 = Tool("水桶")

print(Tool.num)
