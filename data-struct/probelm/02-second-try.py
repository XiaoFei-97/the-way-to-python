#如果a+b+c=1000,且a^2+b^2=c^2（a,b,c为自然数），求出abc所以可能的组合
#运行时间1秒
#
#a = 0
#b = 0
#c = 0
#
import time
#
#start_time = time.time()
#for a in range(1000):
#    for b in range(1000):
#        for c in range(1000):
#            if a+b+c == 1000 and a**2 +b**2 == c**2:
#                print("a=%d,b=%d,c=%d"%(a,b,c))
#end_time = time.time()
#
#print("times:%d"%(end_time-start_time))
#T=1000 * 1000 * 1000 * 2(此处细化是10步)
#时间复杂度T(n) = n^3 * 2
#大O表示法：g(n)=n^3

start_time = time.time()
for a in range(1001):
    for b in range(1001-a):
        c = 1000-a-b
        if a**2 +b**2 == c**2:
                print("a=%d,b=%d,c=%d"%(a,b,c))
#T= 1000 * 1000 * 3 
#时间复杂度T(n) = n^2 *3
#大O表示法：g(n)=n^2
end_time = time.time()

print("times:%d"%(end_time-start_time))
