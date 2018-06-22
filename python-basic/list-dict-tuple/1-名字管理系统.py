#打印功能提示
print("="*50)
print("      名字系统　V8.6")
print("      1:添加用户")
print("      2:删除用户")
print("      3:修改用户")
print("      4:查找用户")
print("      5.查看全部用户")
print("      6.退出系统")
print("="*50)

#存储姓名
names = []

#获取用户的选择
while True:
	num = int(input("请输入功能序号："))
	   
	#根据用户的选择，执行相应的功能
	if num == 1:
		new_name = input("请输入想要添加的姓名：")
		#将new_name添加到列表中
		names.append(new_name)
		print("已添加 %s 到系统中..."%new_name)
		
	elif num == 2: 
		del_name = input("请输入想要删除的姓名:") 
		#将del_name从列表中删除
		names.remove(del_name) 
		print("系统已删除 %s 姓名..."%del_name)

	elif num == 3: 
		change_name = input("请输入想要修改的姓名：")
		#返回修改姓名的下标序号
		name_num = names.index(change_name)
		if name_num >= 0:
			name_change = input("请输入修改后的姓名：") 
			names[name_num] = name_change 
		else:
			print("抱歉，系统中没有你想要修改的姓名...")

	elif num == 4: 
		find_name = input("请输入想要查找的姓名:")
		if find_name in names:
			print("已找到 %s "%name)
		else:
			print("没有找到你想要的人！")

	elif num == 5:
		print(names)

	elif num == 6:
		break

	else:
		print("您的输入有误，请重新输入")
