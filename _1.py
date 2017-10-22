
"""
convention : 전통
----
1. file name, variable = _=temporary, __=내장함수, a, B(x), 1(x) ,&(x)
2. 1-line = 80 charactors, (=recommandation)
3. Indent = 들여쓰기 (4칸 = space), Atom Tab = 4 Spaces
    혼용해서 쓰지 말것
"""

    #first Test
def test1():
    a = 300
    b = 333
    c = a * b

    print(c)                    # 99900
    print('{:,}'.format(c))     # 99,900
# test1()

"""---- for 루프"""
def test2():
    counter = 0
    for n in range(5):
        counter = counter + 1
        print(counter, "Hello python")
    print("END")
# test2()

def t_in_t():
    for n in range(0,13,1):     # range(start=0, end+1, step='1')
        print(n)
# t_in_t()

""" If문 """
def test3(n):
    if n >=5:
        print('greater than 5..')
        print('jackpot')
    else:
        print ('less than 5..')
        print ('try again')
    print('END')

    print('n=', n)
# test3()

""" (3)---- 함수: (definition : 정의)"""
def a_add_b(a,b):
    c = a + b
    return c
# a_add_b(5,9)

#함수 정의
def _a_add_b(a,b):
    c = a + b
    print(c)
# _a_add_b(5,9)
# _a_add_b
# print(_a_add_b)

def test4():
    print('star'in center(31))
test4()
