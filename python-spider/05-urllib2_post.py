#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2 

# 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

# 用户接口
key = raw_input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
formData = {
    "i": key,
    "from": " AUTO",
    "to": " AUTO",
    "smartresult": " dict",
    "client": " fanyideskweb",
    "salt": " 1529564834865",
    "sign": " a7da269e5b0ce434edacdecea8938bb1",
    "doctype": " json",
    "version": " 2.1",
    "keyfrom": " fanyi.web",
    "action": " FY_BY_REALTIME",
    "typoResult": " false",
}

# 表单数据也是需要urllib.urlencode来转码的
data = urllib.urlencode(formData)

# 区分post和get的方式就是查看Request方法里的参数是否有值，那么该方法就是Post
request = urllib2.Request(url,data=data, headers=headers)

response = urllib2.urlopen(request)

print response.read() 


