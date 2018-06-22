class Node(object):
    """定义节点类"""
    def __init__(self,elem):
        """elem表示数据元素,next表示下一个节点的标识"""
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """定义单链表类"""
    def __init__(self,node=None):
        """单链表初始化"""
        self.__head = node 

    def is_empty(self):
        """判断单链表是否空"""
        return self.__head == None

    def length(self):
        """获取单链表长度"""
        #count表示当前计数个数
        count = 0
        #cur表示当前节点的标识
        cur = self.__head
        #如果当前标识为空，则退出循环
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next
        print(end = "")

    def add(self,item):
        """创建一个新的节点"""
        node = Node(item)
        #把这个节点的尾部与头节点相连
        node.next = self.__head
        #让链表头Head指向新的节点
        self.__head = node

    def append(self,item):
        """在尾部添加元素"""
        node = Node(item)
        #判断链表是否为空
        if self.is_empty():
            #如果空，就把节点当做头节点
            self.__head = node
        else:
            cur = self.__head
            #游标没有指向空，就继续循环
            while cur != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        cur = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head 
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node



        





#is_empty()链表是否为空
#length()链表长度
#travel()遍历整个链表
#add(item)链表头部添加元素
#append(item)链表尾部添加元素
#insert(pos,item)指定位置添加元素
#remove(item)删除节点
#search(item)查找节点是否存在
if __name__ == "__main__":
    node = Node(100)
    ll = SingleLinkList()

    print(ll.is_empty())
    ll.insert(2,100)
    ll.append(100)
    ll.travel()
    print(ll.is_empty())
    
