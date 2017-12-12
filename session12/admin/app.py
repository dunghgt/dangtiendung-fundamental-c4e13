from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "jadlakw"

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

@app.route('/admin', methods=['GET', 'POST'])
def  admin():
    if request.method == 'GET': #get form
        return render_template('admin.html', lights=Light.objects())
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

@app.route('/edit/<light_id>', methods=['GET', 'POST'])
def edit(light_id):
    light = Light.objects().with_id(light_id)
    if request.method == 'GET':
        return render_template('edit_light.html', light=light)
    elif request.method == 'POST':
        form = request.form

        title = form['title']
        description = form['description']
        image = form['image']
        price = form['price']

        light.update(title=title, description=description, img=image, price=price)

        flash("Đã sửa thành công~")
        flash("hi")

        return render_template('edit_light.html', light=Light.objects().with_id(light_id))

@app.route('/delete/<light_id>', methods=['GET', 'POST'])
def delete(light_id):
    light = Light.objects().with_id(light_id)
    if request.method == 'GET':
        return render_template('delete_light.html', light=light)
    elif request.method == 'POST':
        form = request.form

        light.delete()

        flash("Xóa thành công")

        return render_template('delete_light.html', light=Light.objects().with_id(light_id))

if __name__ == '__main__':
  app.run(debug=True)
