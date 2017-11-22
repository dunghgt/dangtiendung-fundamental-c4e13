from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    left(36)
    for _ in range(5):
        forward(length)
        left(144)

speed(-1)
for i in range(100):
    import random
    colors = ['blue', 'red', 'pink', 'orange', 'yellow', 'violet']
    color(random.choice(colors))
    x = random.randint(-300, 300)  #random from -300 to 300
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()
