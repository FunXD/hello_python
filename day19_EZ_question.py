import time
import os

""" 문제. 0 ~ n 까지 input()을 받아서 더해라.
# [IN]  몇까지 더할까요? : 100
# [OUT] 정답은 5050 입니다
"""
def test1():
    until=int(input('몇까지 더할까요? '))
    answer = 0
    n=0
    for n in range(until):
        n=n+1
        answer = answer+n
    print('정답은 ',answer, '입니다.')
test1


""" 문제. 스윙스 헬로월드
# 좌우로 0.2초 씩 움직이는 헬로월드를 만들어라
# [OUT]
   |[HELL0]----------| WORLD!
   |----------[HELL0]| WORLD!
"""
def test2():
    sleep = 0
    length = 10
    shape = ' '
    word = 'WORLD'
    while True:
        a=0
        for n in range(length,0,-1):
            front=(shape*n)
            back=(shape*a)
            print('|',front,'[',word,']',back,'|',' WORLD!')
            print('|',back,'[',word,']',front,'|',' WORLD!')
            time.sleep(sleep)
            os.system('cls')
            a=a+1
        a=0
        n=0
        for n in range(length,0,-1):
            front=(shape*a)
            back=(shape*n)
            print('|',front,'[',word,']',back,'|',' WORLD!')
            print('|',back,'[',word,']',front,'|',' WORLD!')
            time.sleep(sleep)
            os.system('cls')
            a=a+1
test2()


""" 문제. 자료 3개의 딕셔너리() 키값, 밸류값을 프린트 해라.
# [IN]  sample_dict = {1:'집', 2:'우산', 3:'자동차'}
# [OUT]
   키값에는 1, 2, 3 = 3개의 자료가 있습니다.
   형식은 <class 'int'>, <class 'int'>, <class 'int'>, 입니다.

   밸류값에는 집, 우산, 자동차 = 3개의 자료가 있습니다.
   형식은 <class 'str'>, <class 'str'>, <class 'str'>, 입니다.
"""
