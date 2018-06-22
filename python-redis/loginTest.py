# coding:utf-8

from MysqllHelper import MysqlHelper
from hashlib import sha1
from redisTest import redisHelper

# 接收输入
name = raw_input("请输入用户名：")
pwd1 = raw_input("请输入密码：")

# 加密
s1 = sha1()
s1.update(pwd1)
pwd2 = s1.hexdigest()

# 查询redis是否存在此用户
r = redisHelper("localhost", 6379)
m = MysqlHelper('localhost', 3306, 'python3', 'root', 'mysql')

if r.get(name) == None:
    sql = 'select passwd from users where name=%s'
    pwd3 = m.one(sql, [name])
    print(pwd3)

    if pwd3 == None:
        print('用户名错误')
    else:
        # 查到了就存放在redis以名字为键和以密码为值进行保存
        r.set(name,pwd3[0])
        # 判断密码是否正确
        if pwd3[0] == pwd2:
            print("成功")
        else:
            print("密码错误")
else:
    if r.get(name) == pwd2:
        print('成功')
    else:
        print('密码错误')



