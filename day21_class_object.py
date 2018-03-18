

""" 클래스 객체/오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
  ** 함수형 프로그래밍 / 객체지향 프로그래밍 = 파이썬 특징의 2축!
  : 클래스 객체 = 흔히 붕어빵 틀(클래스) <--> 붕어빵(인스턴스)에 비유한다.
  :   붕어빵 틀은 1개 인데, 팥-붕어빵, 크림-붕어빵, 다양한 변종을 찍어낸다.
  :   찍어 낸 (인스턴스)는 독립적으로 작동 한다(self)

 1.클래스명 작명 = 파스칼 케이스 (ThisIsPascalCase)
 - 클래스 함수(매서드)의 첫번째 인자 = 인스턴스 자신(Self)
 - 클래스간 띄어쓰기는 2칸 / 함수(매서드)는 1칸 이다.

 2.오브젝트(객체)의 특징! : 클래스 오브젝트 <--> 인스턴스
 - (1) 값 (field) = 클래스변수 or 인스턴스 변수
 - (2) 기능 (method) = 매서드, 매직매서드, 더블언더스코어

 3.클래스만의 매우 특별한 기능
  * 상속 (Inherit) = 부모(Parent) - 자식(Child)
  * 중복 (Override) = 덮어쓰기 / 겹쳐쓰기

 4.'매직 매서드' = '더블 언더스코어' __무엇__ ... '매직' + '매서드' = 뭔가 특별한.
  * 자주쓰는 '매직'
  - __init__ (생성자)  <-->  __del__ (소멸자)
  - __repr__, __str__  : 스트링을 '리턴'
  - __add__, __sub__ ... '연산자'
"""

import _script_run_utf8
_script_run_utf8.main()

""" 만 들려는 매서드, 클래스변수, 인스턴스변수(self)
값 = 클래스변수(성격), 인스턴스변수(이름, 개인비밀)
기능 = 생성자, 소멸자, 연산자
"""

class Human(object):
    total_count = 0
    icon = '무단함'

    def __init__(self,name):
        Human.total_count +=1
        self.name = name

    def say_hello(self,other_obj):
        print('안녕하세요 {}님, 저는 {}입니다'.format(other_obj.name, self.name))

    def say_status(self):
        print("'{}'님의 성격은 '{}'입니다.".format(self.name, self.icon))

class ManOne(Human):
    pass

mo = ManOne('철수')
mo.icon = '영리함'
mo1 = ManOne('영희')
mo1.icon = '난폭함'
mo.say_status()
mo1.say_status()

mo.say_hello(mo1)
mo1.say_hello(mo)

print ('김철수와 신영희의 짧은 인생스토리 시작~~!',('\n'),
'---------------',('\n'),
'김철수와 김영희는 결혼했습니다',('\n'),
'김철수와 김영희는 이혼했습니다',('\n'),
'김철수는 죽었습니다.')


def test1():
    h0 = Human('기본')

    hu = Human('무던한인간')
    hu1 = Human('난폭한 인간')
    hu2 = Human('사랑스러운 인간')


    print(hu.total_count)
    print(hu.icon)
    hu.say_hello(h0)
    hu.say_status()
    print('\n\n')

    hu1.icon ='난폭함'
    print ("COUNT: ", hu1.total_count)
    print ("성격: ", hu1.icon)

    hu1.say_hello(hu)
    hu1.say_status()
    print('\n\n')

    hu2.icon ='사랑스러움'
    print ("COUNT: ", hu2.total_count)
    print ("성격: ", hu2.icon)

    hu2.say_hello(hu1)
    hu2.say_status()
    print('\n\n')
