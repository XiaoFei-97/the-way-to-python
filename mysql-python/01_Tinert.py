# coding:utf-8
from MySQLdb import *
try:
    # host是连接的主机，port是端口，user是用户名，passwd是连接的密码，db是操作数据库名称，charset是编码方式
    conn = connect(host='localhost', port=3306, user='root', passwd='mysql', db='python3', charset='utf8')
    cursor1 = conn.cursor()

    sql = 'insert into Students(sname, passwd) values("jack",123)'

    # 用于执行sql语句
    cursor1.execute(sql)
    print("--3--")
    conn.commit()

    cursor1.close()
    conn.close()
except Exception, e:
    print(e.message)
