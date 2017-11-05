def test1():
    _a = 100
    _b = 3

    _c = _a + _b   # = 103

    _d = _a / _b   # = 33.33333333 'float'
    _e = _a // _b  # = 33 'int'
    _f = _a % _b   # = 1 'int'

    print('_a / _b =',_d)
    print('_a // _b =',_e)
    print('_a % _b =',_f)

    print('ABC', end='')
    print('ABC', end='')
    print('ABC', end='')
    print()
    print('ABC', end='\n\n\n')
    print('ABC', end='\n\n\n')
    print('ABC', end='\n\n\n')
    print()
# test1()

def test2():
    a = 'this'
    b = ' is book'
    c = (a + b +'\n')*1
    print(c)
# test2()

def test3():
    a = "Life is too short, You need python"
    print(len(a))   #14
    print(a[0])     #'L'
    print(a[33])    #'n'
    print(a[-1])
# test3()

def test4():
    """ SLICING """
    print(a[0:4])
    print(a[28:34])
    print(a[-6:])
    print(a[:-6])
    print(len(a[33]))

    b = python
    b = b[:1] + "y" + b[2:]
    print(b)
# test4()

def test5():
    pass

import random
# test5()

def test6():
    a = ['나는', '너는', '천지용은', '이준혁은', '선생님은', '너는', '박근혜는','김정은은']
    a_num = len(a)
    a_rand_num = random.randint(1, a_num)

    b = ['개', '오징어', '최순실', '기저귀', '시계', '초콜릿', '용가리치킨', '핵폭탄']
    b_num = len(b)
    b_rand_num = random.randint(1, b_num)

    c = ['먹는다', '사랑한다', '싫어한다', '와(과) 친구이다', '을(를) 버린다', '때린다','만든다']
    c_num = len(c)
    c_rand_num = random.randint(1, c_num)

    for n in range(50):
        a_num = len(a)
        a_rand_num = random.randint(1, a_num)
        b_num = len(b)
        b_rand_num = random.randint(1, b_num)
        c_num = len(c)
        c_rand_num = random.randint(1, c_num)
        print('%s %s %s'%(a[a_rand_num-1], b[b_rand_num-1], c[c_rand_num-1]))


# test6()
