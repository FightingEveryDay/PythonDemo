import requests
from bs4 import BeautifulSoup as BS
import time


budejie_url = "http://www.budejie.com/"
first_page_url = budejie_url + "text/1"

# set proxy
proxies = {
    "http":"http://113.109.77.30.com:8080/",
    "https":"http://113.109.77.30.com:8080"
}

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers = {'User-Agent': user_agent,
           'Referer': 'http://www.budejie.com/text/1'
}

text_of_each_page = ""

for i in range(100):
    url_of_each_page = budejie_url + "text/" + str(i+1)
    # print url_of_each_page
    r = requests.get(url_of_each_page, headers=headers, proxies=proxies)
    # print r.status_code
    if r.status_code == 200:
        soup = BS(r.text, "lxml")
        text_lists = soup.select('div.j-r-list > ul > li > div.j-r-list-c > div.j-r-list-c-desc')
        for text_of_duanzi in text_lists:
            text_of_each_page += text_of_duanzi.get_text()
        time.sleep(3)
    else:
        continue

myfile = open("budejie.txt", "w")
myfile.write(text_of_each_page.encode('utf-8'))
myfile.close()
