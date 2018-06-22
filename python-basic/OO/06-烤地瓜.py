class patato:
	
	def __init__(self):
		self.cookedstring = "生的"
		self.cookedlevel= 0
		self.condiments = []
	def __str__(self):
		return "地瓜　状态：%s(%s),配料有%s"%(self.cookedstring,self.cookedlevel,str(self.condiments))
	def cook(self,cooked_time):
		#这里的cooked_time一旦被调用完后就会被释放，并没有把上一次烤的时间保存下来
		self.cookedlevel += cooked_time
		if self.cookedlevel >=0 and self.cookedlevel <= 3:
			self.cookedstring = "生的"
		elif self.cookedlevel >3 and self.cookedlevel <= 5:
			self.cookedstring= "半生不熟"
		elif self.cookedlevel >5 and self.cookedlevel <= 8:
			self.cookedstring= "烤好了"
		elif self.cookedlevel >8:
			self.cookedstring = "烤成木炭了"
	def addCondiments(self,item):
		self.condiments.append(item)	

raw_patato = patato()

print(raw_patato)
		
raw_patato.cook(1)
raw_patato.cook(1)
raw_patato.cook(1)
raw_patato.addCondiments("大蒜")
raw_patato.cook(1)
print(raw_patato)
