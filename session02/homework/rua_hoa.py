from turtle import *

left(30)
for i in range(4):
    for k in range(2):
        for j in range(1, 3):
            forward(80)
            right(60*j)
    right(90)


mainloop()
