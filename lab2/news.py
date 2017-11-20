from urllib.request import urlopen
from bs4 import BeautifulSoup

#1. Download HTML content
html = urlopen("http://dantri.com.vn")
html_content = html.read().decode('utf-8')
html.close()

#2. Create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
ul_news = soup.find('ul','ul1 ulnew')
# print(ul_news.prettify())
li_news_list = ul_news.find_all('li')

for li in li_news_list:
    a_detail = li.h4.a
    title = a_detail['title']
    print(title)
    print("-" * 20)
# content = a_detail.string
