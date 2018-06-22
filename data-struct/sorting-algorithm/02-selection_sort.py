#选择排序法
#最优时间复杂度：O（n^2）
#最坏时间复杂度：O（n^2）
#稳定性：不稳定（考虑升序每次选择最大的情况）

def selection_sort(alist):
    """选择排序"""

    n = len(alist)
    for j in range(n-1): # j:0~n-2
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]
       
def main():
    list = [1,5,2,4,7,3,6,2]
    print(list)
    selection_sort(list)
    print(list)


if __name__ == "__main__":
    main()
