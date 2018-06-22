def get_wendu():
	wendu = 22
	print("当前摄氏温度是：%d"%wendu)
	return wendu
def get_huashi_wendu(wendu):
	wendu = wendu + 3
	print("当前华氏温度是：%d"%wendu)
	

result = get_wendu()
get_huashi_wendu(result)

