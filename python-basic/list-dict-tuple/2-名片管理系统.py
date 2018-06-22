#打印功能编号
print("*"*50)
print("     名片系统　V8.0")
print("     1:添加名片")
print("     2:删除名片")
print("     3:修改名片")
print("     4:查找名片")
print("     5:查看所有名片")
print("     6:退出系统")
print("*"*50)

#用来存储程序
users = []
#获取用户输入编号
while True:
	num = int(input("请输入功能序号："))

	#根据用户选择编号，进行相应操作
	if num == 1:
		new_name = input("请添加新名片：")	
		new_qq = input("请添加新qq:")
		new_weixin = input("请添加新weixin:")
		new_number = input("请添加新号码：")

		#定义一个新的字典	
		new_infor = {}
		new_infor["name"] = new_name
		new_infor["qq"] = new_qq
		new_infor["weixin"] = new_weixin
		new_infor["number"] = new_number

		users.append(new_infor)
	elif num == 2:
		del_name = input("请输入需要删除的名片：")
		del_flag = 0
		for temp in users:
			if del_name == temp["name"]:
				print("已删除 %s 的名片"%temp["name"])
				del temp["name"]
				del temp["qq"]
				del temp["weixin"]
				del temp["number"]
				del_flag = 1
				break
		else:
			print("没有找到您要删除的姓名...")
	elif num == 3:
		name = input("请输入需要修改的名片：")	
		for temp in users:
			if name == temp["name"]:
				change_name = input("请输入修改后的名片：")	
				change_qq = input("请输入修改后的qq：")
				change_weixin = input("请输入修改后的weixin：")
				change_number = input("请输入修改后的number：")
				temp["name"] = change_name
				temp["qq"] = change_qq
				temp["weixin"] = change_weixin
				temp["number"] = change_number
				print("%s 已修改成功..."%temp["name"])
			else:
				print("没有找到您需要修改的名片...")
	elif num == 4:
		find_name = input("请输入要查找的姓名：")	
		find_flag = 0	
		for temp in users:
            
				print("%s\t%s\t\t%s\t\t%s\t"%(temp["name"],temp["qq"],temp["weixin"],temp["number"]))
				find_flag = 1
				break
		if find_flag == 0:
			print("抱歉，没有找到您需要的名片...")
	elif num == 5:
		print("姓名\tQQ\t\t微信\t\t电话")
		for temp in users:
			print("%s\t%s\t\t%s\t\t%s\t"%(temp["name"],temp["qq"],temp["weixin"],temp["number"]))
	elif num == 6:
		break	
	else:	
		print("您的输入有误，你输入1－6的序号")
