#!/usr/bin/env python
# coding=utf-8

import urllib2
import random

url = "http://www.baidu.com/"

# 可以是User-Agent列表,也可以代理列表
ua_list = [
    "User-Agent:Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "User-Agent:Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
    "User-Agent:Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "User-Agent:Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"
]

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

# 构造一个请求
request = urllib2.Request(url)

# add_header()方法 添加/修改一个HTTP报头
request.add_header("User-Agent", user_agent)

# get_header()方法 获取一个已有的HTTP报头的值，注意只能是第一个字母大写，其他字母小写
print request.get_header("User-agent")
