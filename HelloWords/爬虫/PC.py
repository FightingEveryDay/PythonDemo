import threading
import urllib.request
import re
import queue

class Wenxue_Spider_Model(threading.Thread):
    "id在set里面,不做任何处理,不在set里面,则put到queue后,add到set里面"
    def __init__(self, queue, firstSourceID, sett, count):
        self.ok = False
        self.firstSourceID = firstSourceID
        self.myqueue = queue
        self.sett = sett
        self.count = count
        self.first_page_url = "http://www.duanwenxue.com/article/307683.html"
        threading.Thread.__init__(self)

    def getHtml(self, url):
        webPage = urllib.request.urlopen(url)
        html = webPage.read()
        webPage.close()
        return html

    def processContent(self, content):
        "去掉内容里面HTML标签"
        re_h = re.compile('</?\w+[^>]*>')
        content = re_h.sub('', content)
        return content

    def getSourceID(self, url):
        "从一个连接里获取到文章的ID"
        re_id = '.*/article/(.*?)\.html'
        sourceID = re.compile(re_id).findall(url)
        print(type(sourceID), "---")
        return sourceID

    def getContent(self, sourceID):
        url = "".join(["http://www.duanwenxue.com/article/",str(sourceID), ".html"])
        print(url)
        html = self.getHtml(url)

        # 这是正则识别内容和链接
        reg = '<div id=.*?class=.*?>\s*<div id="s-article-main01" class=.*?></div>\s*<p>(.*)</p>\s*<div class=.*?>\s*<h3>.*</h3>\s*<p>.*<a href="(.*?)" target="_blank">.*</a></p>\s*<p>.*<a href="(.*?)" target="_blank">.*</a></p>\s*</div>\s*<div id="s-article-main02" class="content-in-bottom"></div>\s*</div>\s*<div class=.*?>\s*<span>.*<a href="(.*?)">.*</a> </span> <span>(.*|.*<a href=(.*?)>.*</a> )</span>'

        self.wenxueContent = re.compile(reg).findall(html)

        for res in self.wenxueContent:
            content = self.processContent(res[0])
            print(content)
            for v in range(1, len(res)):
                thisSourceID = self.getSourceID(res[v])

                for _id in thisSourceID:
                    if _id not in thisSourceID:
                        self.sett.add(_id)
                        self.myqueue.pu(_id)
                        self.count = self.count + 1

                    else:
                        pass

        self.ok = True

    def run(self):
        with True:
            print(self.count)
            if self.myqueue.qsize() > 0:
                sourceid = self.myqueue.get()
                self.getContent(sourceid)



sourceID = "307683"
q = queue.Queue(maxsize = 0)
sett = {"307683"}
count = 1
q.put(sourceID)
Wenxue_Spider_Model(q, sourceID, sett, count).start()
