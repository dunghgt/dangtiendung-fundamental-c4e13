from flask import Flask, render_template
import mlab
from mongoengine import *

app = Flask(__name__)

mlab.connect()

class Light(Document):
    title = StringField()
    img = StringField()
    description = StringField()
    price = StringField()

@app.route('/')
def index():
    data = Light.objects()
    return render_template('index.html', lights=data)

if __name__ == '__main__':
  app.run(debug=True)
