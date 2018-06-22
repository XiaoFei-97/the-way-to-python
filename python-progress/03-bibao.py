#闭包的应用

def test(number):

	print("-----1-----")
	def test_in(number2):
		print("----2-----")
		print(number+number2)
	print("------3------")
	#把函数的引用返回了
	return test_in

#用来接收test(100)，指向类一个函数体,这个100传给了number
ret = test(100)
#这个1传给了number2
ret(1)
ret(100)
ret(200)
