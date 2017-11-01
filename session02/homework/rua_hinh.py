from turtle import *

shape("turtle")

n = int(input("So hinh thich ve: "))
for i in range(3, n + 3):
    for j in range(0, i):
        forward(100)
        left(360/i)

mainloop()
