# _*_ coding:utf-8 _*_

#获取用户要复制的文件名
old_file_name = input("请输入您想要复制的文件：")

#打开要复制的文件
old_file = open(old_file_name,"r")  #！！注意此处不加双引号

#新建一个文件
#new_file_name = "[附件]"+old_file_name
#找到"."后，把复件两个字插入到这个new_file_name中
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position]+"[复件]"+old_file_name[position:]

new_file= open(new_file_name,"w")


#从旧文件中读取数据，且写入到新文件中
while True:
	content = old_file.read(1024)

	if len(content)==0:
		break
	new_file.write(content)

#关闭2个文件
old_file.close()
new_file.close()

'''
f = open("19-交换变量的值.py","r")
content = f.read()

f = open("xxx.txt","w")
f.write(content)
f.close()
'''
