#while 的列表推导
'''
name = []
i=0
while i<=77:
	name.append(i)
	i+=1
print (name)
'''
'''
#for的列表推导,range与切片很类似
for i in range(10,78):
	print(i)
'''

'''
#第一个i是元素的值，后面的for是代表循环的次数，如果第一个i=11，那么所有的元素都是11
a=[i for i in range(1,18)]
print(a)
'''

#for控制循环的次数，for和if的嵌套
c = [i for i in range(10) if i%2==0]
print(c)

#每执行第一个for循环都要执行第二个循环的所有次数
d = [i for i in range(3) for j in range(2)]
print(d)


#每执行第一个for循环都要执行第二个循环的所有次数
d = [(i,j) for i in range(3) for j in range(2)]
print(d)
