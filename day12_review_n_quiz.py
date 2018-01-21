def score():
    kor = (int(input('국어 성적을 입력하십시오 : ')))
    math = (int(input('수학 성적을 입력하십시오 : ')))
    eng = (int(input('영어 성적을 입력하십시오 : ')))

    print ('\n')
    print ('입력받은 숫자')
    print ('------------')
    print ('국어 성적 : ',kor)
    print ('수학 성적 : ',math)
    print ('영어 성적 : ',eng)
    print ('------------')

    average = ((kor+math+eng)/3)
    print ('평균 : %.2f' % (average))
# score()

def circle():
    pi=3.14159265358979323846264338327950288419716939937510
    banji=(int(input('반지름을 입력하십시오 : ')))
    nulbe=(banji*banji*pi)
    dulla=(banji*2*pi)
    print ('반지름 : ',banji)
    print('원의 넓이 : %.3f' % (nulbe))
    print('원의 둘레 : %.3f' % (dulla))
# circle()

def number():
    number=(int(input('다섯 자리 숫자를 입력하십시오 : ')))
    first=(number//10000)
    second=((number//1000)%10)
    third=((number//100)%10)
    fourth=((number//10)%10)
    fifth=(number%10)
    print (first,second,third,fourth,fifth)
    print ('스페이스바를 누르시오')
    input()
# number()
import time
import random
b=0
a=0
for n in range(10000000000000):
    a=random.randint(1,999999999)
    b=random.randint(1,999999999)
    # print(a,'+',b,'=',n+a)
    time.sleep(0.01)
    {:7,}
