try:
	print(num)
	print("-----1-----")

except Exception as ret:
	print("处理异常")
	print(ret)
else:
	print("没有异常才会执行的功能")
finally:
	print("-----finally-----")
