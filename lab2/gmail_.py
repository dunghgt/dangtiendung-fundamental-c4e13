from random import choice
from gmail import *
#
# file_names = ["1.html", "2.html", "3.html"]
# file_name = choice(file_names)

reasons = ["Đau bụng", "Đau đầu", "Đau thận"]
reason = choice(reasons)

template_file = open("1.html", encoding = 'utf-8')
html_content = template_file.read()
template_file.close()
html_content = html_content.replace('{{reason}}', reason)

# print(html_content)

gmail = GMail("dungblabla123@gmail.com", "dung1234")
# msg = Message('~', to = "c4e13.lab.huynq@gmail.com", html = html_content)
msg = Message('~', to = "dungblabla123@gmail.com", html = html_content)
gmail.send(msg)
