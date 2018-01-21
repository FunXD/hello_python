import turtle as tu
import math
import random
import time
tu.speed(0)

def draw_color_bulb(pos_x, pos_y, size=10,width=3, pen='red', fill='yellow'):
    move(pos_x,pos_y+size/2)
    tu.width(width)
    tu.color(pen, fill)
    tu.begin_fill()
    tu.circle(size)
    tu.end_fill()

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

def tu_circle(size):
    tu.circle(size)

def move(x,y):
    tu.penup()
    tu.setpos(x,y)
    tu.pendown()

def pen_width(wide):
    tu.width(wide)

if __name__=='__main__':
    for n in range(900000000000000000000):
        tu.begin_fill()
        tu.width(10)
        tu.color(random.choice(COLOR_PICK))
        tu_circle(random.randint(1,2))
        move(random.randint(-450,450),random.randint(-300,300))
        tu.end_fill()
    tu.mainloop()
