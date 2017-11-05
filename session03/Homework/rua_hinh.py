from turtle import *

shape("turtle")

colors = ["red", "blue", "pink", "green", "orange"]

for (j, i) in enumerate(colors):
    color (i)
    j = j + 3
    for _ in range(j):
        forward(80)
        left(360/(j))

mainloop()
