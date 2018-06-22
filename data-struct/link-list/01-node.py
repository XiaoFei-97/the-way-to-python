#单链表
#构造一个节点

class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

#node = Node(100)
class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        self.__head = None

    def is_empty(self):
        """判断链表为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        #cur游标，来移动遍历节点
        cur = self.__head
        #count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
           print(cur.elem)
           cur = cur.next
        print(end = "")

    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素"
        :pram pos 从0开始
        """
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
            #当循环退出后,pre指向Pos-1
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


node = Node(100)
single_obj = SingleLinkList(node)
single_obj.travel() 



if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.insert(-1,9)
        
    ll.travel()
    ll.remove(8)
    ll.travel()
    print(ll.search(2))
