from flask import Flask, render_template
from mongoengine import *
import mlab

app = Flask(__name__)

#1.connect to mlab
mlab.connect()

#2.design collection
class Light(Document):
    title: StringField()
    img: StringField()
    description: StringField()
    price: StringField()

#3. try to insert a item
a = Light(
        title= "Đèn nhiều màu",
        img= "http://buondenled.com/wp-content/uploads/2016/10/D%C3%A2y-%C4%91%C3%A8n-th%E1%BA%A3-nhi%E1%BB%81u-m%C3%A0u-262x262.jpg",
        description= "Nhiều màu",
        price= "3.000.000 VNĐ"
        )

a.save()

lights = Light.objects()


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
