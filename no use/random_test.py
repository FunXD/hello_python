def test3(n):
    if n >=10:
        print('greater than 10..')
        print('jackpot')
    else:
        print ('less than 10..')
        print ('try again')
    print('END')

    print('n=', n)

import random
for a in range(1):
    n = random.randint(0,10)


test3(n)
