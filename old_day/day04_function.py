import math

def plus_ab(a,b):
    """ This is plus a by B
     a = int, b = int
    """
    return a, b, a+b

def minus_ab(a,b):
    """ This is minus a by B
     a = int, b = int
    """
    return a, b, a-b

def multi_ab(a,b):
    """ This is multi a by B
     a = int, b = int
    """
    return a, b, a*b

def nanum_ab(a,b):
    """ This is divide a by B
     a = int, b = int
    """
    return a, b, a/b

def math_sqrt_ab(a,b):
    """ This is sqrt(a)
     a = int
    """
    return a, b, math.sqrt(a)

def math_pi_ab(a,b):
    """ This is a * pi
     a = int
    """
    return a, b, math.pi*a

while True:

    _ans1 = int(input('a = '))
    _ans2 = int(input('b = '))
    _choose = int(input('choose (1 = +, 2 = -, 3 = x, 4 = / 5 = sqrt 6 = pi) = '))

    if _choose==1:
        _a, _b, c = plus_ab(_ans1, _ans2)
        print(c)

    if _choose==2:
        _a, _b, c = minus_ab(_ans1, _ans2)
        print(c)

    if _choose==3:
        _a, _b, c = multi_ab(_ans1, _ans2)
        print(c)

    if _choose==4:
        _a, _b, c = nanum_ab(_ans1, _ans2)
        print(c)

    if _choose==5:
        _a, _b, c = math_sqrt_ab(_ans1, _ans2)
        print(c)

    if _choose==6:
        _a, _b, c = math_pi_ab(_ans1, _ans2)
        print(c)
