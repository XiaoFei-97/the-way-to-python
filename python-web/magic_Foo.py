#_*_ coding:utf-8 _*_
#魔法方法创建类

class Foo(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item)
        return self

    def __str__(self):
        return ""

# obj = Foo()
# "think"obj.think
# obj.diffrernt

print(Foo().think.different.itcast)

# think different itcast