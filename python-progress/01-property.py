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

	def setNum(self,new_num):
		print("------setter------")
		self.__num = new_num

	def getNum(self):
		print("------getter-----")	
		return self.__num

	num = property(getNum,setNum)

t = Test()
t.setNum(50)

#以下两种print结果相同,返回结果
print(t.getNum())
print(t.num)
print("*"*50)

#这两个用法相同，用来设值，这就是property的好处
t.setNum(50)
t.num = 20
print(t.num)
