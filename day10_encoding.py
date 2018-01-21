import time
import sys
def test1():
    n=0
    for n in range(10):
        print (n,end='', flush=True)
        time.sleep(0.5)
        n=n+1
# test1()

def test2():
    import _script_run_utf8
    _script_run_utf8.main()
    print('안녕세계')
    print(sys.getdefaultencoding())
    print(sys.stdout.encoding)
    print(sys.stderr.encoding)
# test2()


def test3():
    _year = '갑을병정무기경신임계'
    _number = '4567890123'
    _zodiac = '자축인명진사오미신유술혜'

    _a = zip(_number,_year)
    print(_a)
    print(list(_a))

    _a = zip(_number,_year)
    print(dict(_a))

    _a = zip(_number,_year)
    print(tuple(_a))

    _a = zip(_number,_year)
    print(set(_a))
# test3()






def compare():
    _a = (lambda x, y: x**2+y**2)(4,3)
    print('lambda = %s'%_a)

    def tempo(x,y):
        return(x**2 + y**2)
    _b = tempo(4,3)
    print('function = %s'%_b)
compare(4,3)
compare(2,1)
compare(5,7)
compare(6,9)
