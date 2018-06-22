#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import urllib2

# User-Agent 是爬虫与反爬虫斗争的第一步
headers = {
    "User-Agent": " Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
}
# 通过urllib.Request来构造一个请求对象
request = urllib2.Request("http://www.baidu.com/", headers=headers)
# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# 服务器返回的类文件对象支持python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串

# 打印 响应内容
# print response.read()

# 返回 HTTP的响应码，成功返回200，不成功
print response.getcode()

# 返回 返回实际数据的具体URL，防止重定向问题
print response.geturl()

# 返回 服务器响应的HTTP报头
print response.info()

"""
# 爬去静态页面只要写User-Agent就行
GET / HTTP/1.1
headers:
Host: www.baidu.com
# 可以不需要长连接
Connection: keep-alive

Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
# 不能暴露自己的IP 
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36
# 表示文本接收的数据类型，默认可以不写 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
#Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

# 跟登录相关的基本用cookie处理
Cookie: BAIDUID=15D791ACF6F5F54258D454FF0F126591:FG=1; BIDUPSID=15D791ACF6F5F54258D454FF0F126591; PSTM=1526091310; BD_UPN=123353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=dOTWlPNGptbTNGdkxxa0xWNFhocWxlfmIxdkxEbzNOQXU2bjlBdkx0WWN-VTViQVFBQUFBJCQAAAAAAAAAAAEAAABgf2iRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABxwJ1sccCdbQm; BD_HOME=1; H_PS_PSSID=1440_21109_26350_20928; BD_CK_SAM=1; PSINO=7; H_PS_645EC=9bd10C0itfshZzOfC2qqaKfjAt1PBA43TJOfkUc9xRb7ANPy%2B6jIJr4TKdo
"""
