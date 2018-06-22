#coding=utf-8
#获取用户输入
date = int(input("请输入１～７的数字"))
#判断用户的数据，并且显示对应的信息
if date == 1:
	print("星期一")
elif date == 2:
	print("星期二")
elif date == 3:
	print("星期三")
elif date == 4:
	print("星期四")
elif date == 5:
	print("星期五")
elif date == 6:
	print("星期六")
elif date == 7:
	print("星期天")
else:
	print("你的输入有误，请输入１～７的数字")
