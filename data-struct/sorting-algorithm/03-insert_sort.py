#插入排序法
#最优时间复杂度：O(n)（升序排列，序列已处于升序状态）
#最坏时间复杂度：O(n^2)
#稳定性：稳定

def insert_sort(alist):
    """插入排序"""
    for i in range(1,len(alist)):
        #从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]

def main():
    list = [1,2,5,6,4,8,9,7]
    print(list)
    insert_sort(list)
    print(list)

if __name__ == "__main__":
    main()
    


