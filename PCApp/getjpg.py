#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# print getHtml("http://www.baidu.com")

import re
def getImage(html):
    reg = "百度一下"
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)

    print imglist

    return
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

html = getHtml("https://www.cnblogs.com/")

print getImage(html)
