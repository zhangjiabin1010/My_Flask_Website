import requests
from bs4 import BeautifulSoup
def url_list():
    content_list = []
    for page in range(1,18):
        urls = 'http://www.zdfans.com/apk/page/'+str(page)
        res = requests.get(urls)
        text = res.text
        soup = BeautifulSoup(text,"lxml")
        list1=soup.find('ul',attrs={'class':'excerpt'})

        for a_li in list1.find_all('li'):
            a_href = a_li.find_all('a')
            url = a_href[1]['href']
            content_dict = contentparse(url)
            content_list.append(content_dict)
            print(content_list)
    return content_list

def contentparse(url):
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text, 'lxml')
    title = soup.find('h1', attrs={'class': 'meta-tit'}).find('a').getText()
    time = soup.find('p', attrs={'class': 'meta-info'}).contents[0][1:11]
    context = str(soup.find('div',attrs={'class':'entry'}))
    content_dict = {'title':title,'time':time,'context':context}
    return content_dict
if __name__ == '__main__':
    url_list()





