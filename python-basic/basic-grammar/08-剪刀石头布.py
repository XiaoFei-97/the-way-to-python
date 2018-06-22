i = 1
while i<=3:

	#导入随机random
	import random
	computer = random.randint(0,2)
	#提醒用户进行输入
	player = int(input("请输入　0剪刀　1石头　2布："))

	#判断用户的输入，然后显示对应的输出结果
	if player == computer:
		print("游戏平局，开始下一场吧！") 
	elif (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
		print("你输了，准备下一局把！")
	else:
		print("你赢了小帅哥！")
	i+=1
