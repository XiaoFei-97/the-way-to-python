#num = property(setNum,getNum)
#将方法转换为只读
#注意点:
#1.Num到底是调用getNum()还是setNum(),要根据实际的场景来判断
#2.如果是给t.num赋值，那么一定调用setNum()
#3.如果是获取t.num的值，那么就一定调用getNum()

#property的作用:相当于把方法进行了封装，开发者在对属性设置数据的时候更方便

class Test(object):
	def __init__(self):
		self.__num = 100

	@property #修饰器
	def num(self):
		print("------getter-----")	
		return self.__num
		
	@num.setter #修饰器
	def num(self,new_num):
		print("------setter------")
		self.__num = new_num


t = Test()

t.num = 20 #相当于调用了t.setNum()

print(t.num) #相当于调用了t.getNum()
