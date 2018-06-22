#冒泡法排序
#最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
#最坏时间复杂度：O(n2)
#稳定性：稳定

def bubble_sort(alist):
    """冒泡排序"""
    for j in range(len(alist)-1,0,-1):
        #count表示交换次数
        count = 0
        #j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            #班长从头走到尾
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if 0==count:
            return

def main():
    list = [1,5,2,1,3,6]
    print(list)
    bubble_sort(list)
    print(list)

if __name__ == "__main__":
    main()
