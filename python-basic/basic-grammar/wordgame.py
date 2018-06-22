mport random
secert = random.randint(1,10)
print("文字游戏")
temp = input("请输入你想要的数字把：")
guess = int(temp)
if guess == 8:
	print("你猜对了")
else:
	print("sorry!")
