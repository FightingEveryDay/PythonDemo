import urllib.request
from bs4 import BeautifulSoup
import requests.packages.urllib3.util.ssl_

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

# 网址
url = "https://www.baidu.com/link?url=qiGen9MsLzEvfahJAJ0n7DBH1KAXZ_gNSjwhZzmClP3&wd=&eqid=b50bec6f00033204000000065a4c3365"

# 请求
def getRequest(url):

    request = urllib.request.Request(url)

    return request

# 响应
def getResponse(url,request):
    if url:
        request = getRequest(url)
    response = urllib.request.urlopen(request)
    return response

# 爬取结果
# response = urllib.request.urlopen(request)

def getData(url):

    data = getResponse(url,None).read()

    return data

# 设置解码方式
# data = data.decode('utf-8')

# print(data)
data = getData(url)
print(data)

soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify())
# print('------>'+str(soup.body.div.div))
# print(type(soup.body.div.div))
# print(soup.body.container)
# print(soup.find_all('a'))
listSoup = soup.find_all('a')
urlArray = []
for link in listSoup:
    # print(link.string)
    if link.string == '地址1':
        # data = getData(link.url)
        # print(link.get('href'))
        dataUrl = link.get('href')

        request = getRequest(dataUrl)
        response = getResponse(None,request)
        print(response)
    #     # print(str(data))
    #     pass


f = open("doubanFlie", 'w')
f.write(str(data, encoding='utf-8'))
f.close()