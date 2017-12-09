from flask import Flask, render_template, request
import mlab
from mongoengine import *

app = Flask(__name__)

mlab.connect()

class Light(Document):
    title = StringField()
    img = StringField()
    description = StringField()
    price = IntField()

@app.route('/')
def index():
    data = Light.objects()
    return render_template('index.html', lights=data)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'GET': #get form
        return render_template('add_item.html')
    elif request.method == 'POST': #receive form
        # 1 Extract data in form
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']
        # 2 Add into database
        new_item = Light(title=title, img=image, description=description, price=price)
        new_item.save()
        return render_template('complete.html')


if __name__ == '__main__':
  app.run(debug=True)
