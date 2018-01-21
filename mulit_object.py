import turtle as tu

_b = tu.Turtle()
_b.speed(0)



COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

_b.speed('fastest')

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

go(_b, 100, 90)
go(_b, 100, -90)

go(_b, 100, 90)
go(_b, 100, -90)

go(_b, 100, 90)
go(_b, 100, -90)

_a = tu.Turtle()
_a.color('red','green')
_a.width(10)

go(_a, 100, -90)
go(_a, 100, 90)

go(_a, 100, -90)
go(_a, 100, 90)

go(_a, 100, -90)
go(_a, 100, 90)
