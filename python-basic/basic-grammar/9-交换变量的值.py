#_*_ coding:utf-8 _*_

a = 3
b = 4

#第一种交换方式，需要第三个变量
#c = 0
#c = a
#a = b
#b = c

#第二种交换方式，不需要第三个变量
#a = a+b
#b = a-b
#a = a-b

#第三种交换方式，也不需要第三个变量
a,b = b,a
print("a=%d,b=%d"%(a,b))
