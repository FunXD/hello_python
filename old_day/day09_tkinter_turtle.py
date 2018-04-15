import turtle as tu
import random
import math

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

tu.speed('fastest')

def move(obj, pos_x=0, pos_y=0):
    obj.penup()
    obj.setx(pos_x)
    obj.sety(pos_y)
    obj.pendown()

def go(obj, go, angle=0):
    """
    go=forward
    angle=turn: left=minus 180 / right= plus 180
    """
    obj.forward(go)
    obj.right(angle)

def star(obj, pos_x, pos_y, size=10, width=1, trailing=False):
    obj.width(width)
    if trailing:
        obj.setx(pos_x)
        obj.sety(pos_y)
    else:
        obj.penup()
        obj.setx(pos_x)
        obj.sety(pos_y)
        obj.pendown()

    obj.begin_fill()
    obj.left(90+126)
    for i in range(5):
        obj.forward(size)
        obj.right(144)
        obj.forward(size)
        obj.left(72)
    obj.end_fill()
    obj.setheading(0)


star(tu, 0, 0, 50, 3)

_DEG = 40
_L=40
_radian = math.radians(degree)

_S = go()
_H = _l * math.tan(_radian)

def draw_triangle(pos_x, pos_y, lowerside, sameside, angle=40):
    tu.penup()
    tu.setx(pos_x)
    tu.sety(pos_y)
    tu.pendown()
    tu.right(angle)
    go(sameside, 360-angle)
    go(lowerside, angle)
    tu.forward(sameside)
    tu.right(angle)
draw_triangle(0, 300, 50, math.cos(math.radians(40)))

def tree_trunk(pos_x, pos_y, forward,width):
    tu.width(width)
    tu.pencolor('brown')
    tu.setx(pos_x)
    tu.sety(pos_y)
    tu.right(90)
    tu.forward(forward)
tree_trunk(0,-70,80,20)



tu.mainloop()
