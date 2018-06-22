#用来存储信息
users = []

def print_functions():
	"""打印功能编号"""
	print("*"*50)
	print("     名片系统　V8.0")
	print("     1:添加名片")
	print("     2:删除名片")
	print("     3:修改名片")
	print("     4:查找名片")
	print("     5:查看所有名片")
	print("     6.保存文件")
	print("     7:退出系统")
	print("*"*50)

def add_user():
	"""添加一个新名片"""
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
	global users
	users.append(new_infor)

def sub_user():
	"""删除一个名片"""
	del_name = input("请输入需要删除的名片：")
	i = 0

	for temp in users:
		i+=1
		if del_name in temp['name']:
			print('删除的名片已找到')
			break
	#删除列表中的字典
	del users[(i-1)]
	print('删除的名片已删除')

def change_user():
	"""修改一个名片"""
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
			
def find_user():
	"""查找一个名片"""
	global users
	find_name = input("请输入要查找的姓名：")	
	find_flag = 0	
	for temp in users:
		if find_name == temp["name"]:
			print("%s\t%s\t\t%s\t\t%s\t"%(temp["name"],temp["qq"],temp["weixin"],temp["number"]))
			find_flag = 1
			break
	if find_flag == 0:
		print("抱歉，没有找到您需要的名片...")

def check_user():
	"""查询所有名片"""
	global users
	print("姓名\tQQ\t\t微信\t\t电话")
	for temp in users:				
		if temp in users:
			print("%s\t%s\t\t%s\t\t%s\t"%(temp["name"],temp["qq"],temp["weixin"],temp["number"]))

def save_2_file():
	"""创建一个文本，保存当前的文本内容"""
	f = open("backup.data","w")
	f.write(str(users))
	f.close()

def load_file():
	"""从保存的文本中读取内容"""
	#try是为了避免在移植过程中可能没有backup.data的情况会出现异常
	'''在修改全局变量时，一定要用global声明一下'''
	global users
	try:
		f = open("backup.data")
		users = eval(f.read()) 
		f.close()
	except Exception:
		pass
#退出系统
#def pop_system():
#	break

#获取用户输入编号
def main():
	"""完成对整个程序的控制"""
	load_file()
	print_functions()
	while True:
		num = int(input("请输入功能序号："))
		#根据用户选择编号，进行相应操作
		if num == 1:
			add_user()
		elif num == 2:
			sub_user()
		elif num == 3:
			change_user()
		elif num == 4:
			find_user()
		elif num == 5:
			check_user()
		elif num == 6:
			save_2_file()
		elif num == 7:
			#pop_system()
			break
		else:	
			print("您的输入有误，你输入1－6的序号")

if __name__ == "__main__":
	main()
