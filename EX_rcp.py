
import random
rock = 1
sissers = 2
paper = 3
def is_playing_stop():
    _a_str = input("더 하시겠습니까? (y/n)")
    if _a_str.lower().startswith('n'):
        return True
    else:
        return False
        count = 0

def who_win():
    eq = me - com
    if eq == 0:
        print ('무')
    elif eq == 1 or eq == -2:
        print ('패')
    elif eq == -1 or eq == 2:
        print ('승')

for n in range (20):
    me = random.randint(1,3)
    com = random.randint(1,3)
    n+1,'.',me,'/',com,'/'
    who_win()
print('\n')
