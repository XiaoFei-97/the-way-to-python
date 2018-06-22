#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib


def LoadPage(url, filename):
    """
        作用：根据url发送的请求，获取服务器的响应文件
        url:需要爬去的url地址
        filename: 处理的文件名
    """
    print "正在下载" + filename
    headers = {"User-Agenr": "User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()
    
def WritePage(html, filename):
    """
        作用：将html内容写入到本地
        html：服务器响应的文件内容
    """
    print "正在写入" + filename
    with open(filename, "w") as f:
        f.write(html)
    print "-" * 30

def TieBaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫的调度器，负责组合处理每个页面的URL
        url: 贴吧url的前部分
        beginPage: 起始页
        endPage: 终止页
    """
    for page in range(beginPage, endPage+1):
        pn = str((page - 1)*50)
        
        filename = "第" + str(page) + "页.html"

        fullurl = url + "&pn=" + pn
        print(fullurl)
        html = LoadPage(fullurl, filename)
        WritePage(html, filename)


if __name__ == "__main__":
    kw = raw_input("请用户输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入起始页:"))
    endPage = int(raw_input("请输入结束页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})

    fullurl = url + key

    TieBaSpider(fullurl, beginPage, endPage)
