from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
html_content = html.read().decode('utf8')
html.close

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table',id = 'tableContent')


tr_list = table.find_all('tr' )
for tr in tr_list:
    td_list = tr.find_all('td')
    for td in td_list:
        content = td.string
        if content != None:
            print(content)
