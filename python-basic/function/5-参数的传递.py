def input_nums():
	first_num = int(input("请输入第一个数字："))
	second_num = int(input("请输入第第二个数字："))
	third_num = int(input("请输入第三个数字："))
	return first_num,second_num,third_num
def print_add_nums(first_num,second_num,third_num):
	#first = nums[0]
	#second = nums[1]
	#third = nums[2]
	n = len(nums)
	add_num = (first_num + second_num + third_num) /n
	print("三个数字分别为%d,%d,%d"%(first_num,second_num,third_num))
	print("(%d+%d+%d)/%d=%d"%(first_num,second_num,third_num,add_num,n))
nums = input_nums()
print_add_nums(nums[0],nums[1],nums[2])

