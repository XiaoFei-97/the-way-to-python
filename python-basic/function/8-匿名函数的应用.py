#coding=utf-8
#_*_coding:utf-8_*_

def test(a,b,func):
	result = func(a,b)
	return result
func_new = input("请输入一个匿名函数：")
#python2的版本需要用eval转换为公式，而python3不需要
#func_new = eval(func_new)#eval表示将任何的输入都转化成公式
num = test(11,22,func_new)
print(num)
