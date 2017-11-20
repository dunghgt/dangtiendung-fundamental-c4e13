from urllib.request import urlopen
from bs4 import BeautifulSoup

zing = urlopen("http://nhaczingmp3.com/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html")
zing_content = zing.read().decode("utf8")
zing.close()

soup = BeautifulSoup(zing_content, 'html.parser')
div = soup.find('div', 'widget-box')
ul = div.ul
# print(ul)

li_list = ul.find_all('li', 'song')
for li in li_list:
    div = li.find('div', 'list-body')
    a_detail = div.h3.a
    content = a_detail.string.replace("  ",'')
    print(content)
    print('-' * 20)
