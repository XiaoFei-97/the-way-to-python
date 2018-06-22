#5!=5*4*3*2*1
#4!=$*3*2*1

'''
i=1
result = 1
while i<5:
	result = result*i
	i+=1
print(result)
'''

#5! =>> 5*4!
#4! =>> 4*3!

'''
def xxx(num)
	num*xxxx(num-1)

def xx(num)
	num*xxx(num-1)

def getnums(num)
	num*xxx(num-1)
'''

def getNums(num):
	if num>1:
		#此处注意要有返回值到下一个调用的函数中
		return num*getNums(num-1)
	else:
		return num
result = getNums(4)
print(result)
