#双端队列的实现

class Dqueue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self,item):
        """往队头中添加一个item元素"""
        self.__list.insert(0,item)

    def add_rear(self,item):
        """往队尾中添加一个item元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队头删除一个元素"""
        self.__list.pop(0)

    def pop_rear(self):
        """从队尾删除一个元素"""
        self.__list.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

if __name__ == "__main__":
    s = Dqueue()
    print(s.is_empty())
    s.add_front(1)
    s.add_front(2)
    s.add_rear(3)
    s.add_rear(4)
    print(s.size())
    print(s.pop_rear())
