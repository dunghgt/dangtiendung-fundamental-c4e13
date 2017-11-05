from turtle import *

colors = ["blue", "red", "orange", "pink", "grey"]

for i in colors:
    color(i)
    begin_fill()
    for x in range(2):
        for j in range(1, 3):
            forward(40*j)
            left(90)
    forward(40)
    end_fill()

mainloop()
