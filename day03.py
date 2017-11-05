import random


def test1():
    print(dir(random))

    for n in dir(random):
        print(n)
# test1()


def test2():
    """rantint"""
    for n in range(30):
        a = random.randint(0,10)
        print(a)
# test3()

def test3():
    a = random.choice('ABCDEFG')
    a = random.choice([1,2,3,4])
#test3()

def test4():
    a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    a = [n for n in range(50) if n%2 == 0]
    for n in range(50):
        random.shuffle(a)
        print(a)
# test4()


counter =0
URname = input('Your Name = ')
intro ='어서오라 %s 용사여.\n숫자를 맞춰야 탈출할 수 있다.\n10번내로 맞춰야한다네.\n잘해보시게나'
print(intro % (URname))
b = random.randint(1,100)

while True:
    counter = counter+1
    if counter > 10:
        print('Mission Failed')
        break
    a = int(input('Guess number = '))

    if a == b:
        print('CORRECT!')
        break
    elif a < b:
        print('small')

    elif a > b:
        print('big')














print(a)
