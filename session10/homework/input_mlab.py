from mongoengine import *
import mlab

#1.connect to mlab
mlab.connect()

#2.design collection
class Light(Document):
    title= StringField()
    img= StringField()
    description= StringField()
    price= StringField()

    #3. try to insert a item
while True:
    a = Light(
        title= input("title: "),
        img= input("img: "),
        description= input("des: "),
        price= input("Price: ")
        )

    a.save()

    lights = Light.objects()
