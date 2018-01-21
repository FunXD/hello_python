def first():
    work = (int(input('근무 시간을 입력하십시오 : ')))
    money = (int(input('시간당 수당을 입력하십시오 : ')))
    give = work*money
    if work>12:
        give = give+((work-12)*(money*0.3))
    print ('총 급여는', format(give,','), '원입니다.')

    while True:
        repeat = (input('엔터를 눌러 다시'))
        if repeat == '':
            print ('\n')
            work = (int(input('근무 시간을 입력하십시오 : ')))
            money = (int(input('시간당 수당을 입력하십시오 : ')))
            give = work*money
            if work>12:
                give = give+((work-12)*(money*0.3))
            print ('총 급여는', format(give,','), '원입니다.')
        else:
            break
# first()

def second():
    number = (int(input('정수를 입력하십시오 : ')))
    a=1
    for n in range(number):
        if number%a==0:
            print (a,'\n')
            a=a+1

        else:
            a=a+1
    while True:
        repeat = (input('엔터를 눌러 다시'))
        if repeat == '':
            print ('\n')
            number = (int(input('정수를 입력하십시오 : ')))
            a=1
            for n in range(number):
                if number%a==0:
                    print (a,'\n')
                    a=a+1
                else:
                    a=a+1
        else:
            break
# second()

def third():
    first = (int(input('정수를 입력하십시오 : ')))
    second = (int(input('정수를 입력하십시오 : ')))
    third = (int(input('정수를 입력하십시오 : ')))
    fourth = (int(input('정수를 입력하십시오 : ')))
    fifth = (int(input('정수를 입력하십시오 : ')))

    max=first
    for n in range(5):
        if max<second:
            max=second
        if max<third:
            max=third
        if max<fourth:
            max=fourth
        if max<fifth:
            max=fifth
    print('가장 큰 값 : ',max)

    while True:
        repeat = (input('엔터를 눌러 다시'))
        if repeat == '':
            print('\n')
            first = (int(input('정수를 입력하십시오 : ')))
            second = (int(input('정수를 입력하십시오 : ')))
            third = (int(input('정수를 입력하십시오 : ')))
            fourth = (int(input('정수를 입력하십시오 : ')))
            fifth = (int(input('정수를 입력하십시오 : ')))

            max=first
            for n in range(5):
                if max<second:
                    max=second
                if max<third:
                    max=third
                if max<fourth:
                    max=fourth
                if max<fifth:
                    max=fifth
            print('가장 큰 값 : ',max)
        else:
            break
# third()
