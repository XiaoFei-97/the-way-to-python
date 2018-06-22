#九九乘法表
i = 1#行
while i<=9:

	j = 1#列
	while j<=i:
		print("%d*%d=%d\t"%(j,i,j*i),end=" ")
		j +=1
	print(" ")
	i += 1
