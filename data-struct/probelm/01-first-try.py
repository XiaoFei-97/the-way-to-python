#如果a+b+c=1000,且a^2+b^2=c^2（a,b,c为自然数），求出abc所以可能的组合
#运行时间191秒

#a = 0
#b = 0
#c = 0

import time

start_time = time.time()
for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if a+b+c == 1000 and a**2 +b**2 == c**2:
                print("a=%d,b=%d,c=%d"%(a,b,c))
end_time = time.time()

print("times:%d"%(end_time-start_time))
