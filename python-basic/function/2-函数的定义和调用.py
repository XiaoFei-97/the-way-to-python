#定义一个函数为print_shape
def print_shape():
	i = 1 

	#用来控制行数为5行
	while i<=5:
		j = 1 
		
		#用来控制列数最多为5列
		while j<=i:
			#打印之后不换行
			print("*",end = " ")
			j+=1

		#打印之后就换行
		print(" ")		
		i+=1

#用来执行函数
print_shape()
