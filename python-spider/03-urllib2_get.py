#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib

url = "http://www.baidu.com/s"
headers = {"User-Agent": "Mozilla...."}

# python2中使用raw_input
keyword = raw_input("请输入需要查询的关键:")

# 字典形式存储，转url编码后就可成为"wd=xxx"
wd = {"wd": keyword}
# 使用urllib.urlencode来进行url的关键字编码
wd = urllib.urlencode(wd)
# 使用urllib.unquote来进行url的关键字解码
# urllib.unquote("wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2")

# 拼接字符，作为最后的请求URL111
full_url = url + "?" + wd

# 构造一个request的请求
request = urllib2.Request(full_url, headers=headers)

# 返回 一个类文件对象 
response = urllib2.urlopen(request)

# 打印 响应内容 
print response.read()
