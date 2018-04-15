def test3(n):
    if n >=20:
        print('greater than 20..')
        print('jackpot')
    else:
        print ('less than 20..')
        print ('try again')
    print('END')

    print('n=', n)

import random
for a in range(1):
    n = random.randint(0,20)


test3(n)
