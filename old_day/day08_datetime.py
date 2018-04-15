
# import os
# import time
# import datetime
""" Refer : DATETIME module Documentation
 - format here : https://docs.python.org/2/library/datetime.html
(1) datetime, time module
(2) recursive functions - countdown, factorial, fibonacci(yield)
(3)
"""

def clock():
    while True:
        _time = datetime.datetime.now()
        _time.strftime('')
        ampm = _time.strftime('%p')
        hour = _time.strftime('%H')
        minute = _time.strftime('%M')
        second = _time.strftime('%S')
        weekend = _time.strftime('%A')
        _time_format = _time.strftime('%p %H : %M : %S - %A ')
        print(_time_format)
        time.sleep(1)
        os.system('cls')
# clock()



def numbercount():
    for n  in range(10, -1, -1):
        print(n)
        time.sleep(0.2)
        os.system('cls')
    print('Fire!')
    print()

    def countdown(start_number):
        if start_number >= 0:
            print(start_number)
            time.sleep(0.2)

            countdown(start_number-1)
        else:
            print('Fire!')
    countdown(10)
# numbercount()

def get_factorial(number):
    """ FACTORIAL = 5! = 5 * 4 * 3 * 2 * 1
    GF(3) = 3 * GF(2)
                2 * GF(1)
                     1
    there for, GF(4) = 4 * 3 * 2 * 1
    """

    if number != 1:
        return number * get_factorial(number -1)
    else:
        return 1

    _a = get_factorial(10)
    print(_a)
# get_factorial()

def show_factorial(number):
    _equation = str(number)
    _value= get_factorial(number)

    for i in range(number-1 ,0 ,-1):
        _equation += ' x ' + str(i)
    print('{}! = {} = {:,}'.format(number, _equation, _value))
# show_factorial(10)


def get_fibonacci(times):
    if times > 1:
        a, b = 0, 1
        for n in range(times -1):
            a, b = b, a+b
        return b
    elif times <= 1:
        return times

    _a = get_fibonacci(3)
    print(_a)
# get_fibonacci()

# def show_fibonacci():
#     for n in range(50):
#         _a = get_fibonacci(n)
#         if n <= 1:
#             print('{:3}={:15,}, '.format(n, _a), end '\n')
# show_fibonacci()

# def wait_esc():
#     input("Enter to esc ----->\n\n")
#
# import sys
import turtle

def turtle_go(go, left=0, right=0):
    turtle.forward(go)
    turtle.left(left)
    turtle.right(right)

n = 200
a = 200
for n in range(100):
    turtle_go(n,a,0)
    n=n+50
    a=a-50
turtle.mainloop()
