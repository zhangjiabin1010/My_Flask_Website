import requests
from bs4 import BeautifulSoup
import re

def url_list2():
    content = []
    for page in range(1,5):
        urls = 'https://laod.cn/news/page/'+str(page)
        res = requests.get(urls)
        text = res.text
        soup = BeautifulSoup(text,"lxml")
        list2 = soup.find_all('article',class_=('wow'))
        for href in list2:
            a_href = href.find('a')
            url = a_href['href']
            content_dict = contentparse(url)
            content.append(content_dict)
            print(url)
            print(content)
    return content
def contentparse(url):
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text,'lxml')
    title = soup.find('h1',attrs={'class':'entry-title'}).getText()
    reg = '([0-9]{4})-([0-9]{2})-([0-9]{2})'
    data = soup.find('ul',attrs={'class':'spostinfo'}).getText()
    time = re.search(reg,data).group()
    context1 = str(soup.find('div',attrs={'class':'single-content'}))
    context = re.sub('<a(.*?)>',"",context1.replace('>\n','>').replace('single-content','entry').replace('</a>','')).replace('<p>','<p><span>').replace('</p>','</span></p>')

    content_dict = {'title':title,'time':time,'context':context}
    return content_dict
if __name__ == '__main__':
    url_list2()






