#*args不定参数，可代表33,44
def sum_2_nums(a,b,*args):

	#获取args元组的长度
	long=len(args)
	print(long)

	i=0
	sum=0
	#循环long次，得出答案
	while i<long:
		sum=sum+args[i]
		i+=1
	result = a+b+sum
	#result = a+b
	#for num in args:
		#result+=num

	print("%d"%result)
sum_2_nums(11,22,33,44)
