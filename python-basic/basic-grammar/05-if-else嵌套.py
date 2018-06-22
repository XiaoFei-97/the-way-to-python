sex = input("输入你的性别：")#男或者女

if sex == "男":
	height = input("你高吗?")
	money = int(input("输入你现在的全部资产："))#大于1000000为富
	handsome = input("你帅吗？")
	
	if height == "高" and money>=1000000 and handsome == "帅":
		print("高富帅.....")
	else:
		print("对不起，你不是高富帅")
if sex == "女":
	color = input("你白吗？")
	money = int(input("输入你现在的全部资产："))#大于1000000为富
	beauty = input("你美吗？")

	if color == "白" and money>=1000000 and beauty == "美":
		print("白富美.....")
	else:
		print("对不起，你不是白富美哦。")
	
