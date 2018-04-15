SEPERATOR = '\n' + '__'*30 + '\n\n'

def test1():
    print('a=', ord('a'))               # 97
    print('A=', ord('A'), SEPERATOR)    # 65

    print('chr(97)', chr(97))           # 'a'
    print('chr(65)', chr(65), SEPERATOR)# 'A'
# test1()

def test2():
    counter = 0
    for n in range(1, 128):
        # print(n,chr)(n),'\t', end='',)
        counter = counter + 1           # counter += 1
        if counter == 5:
            print(('%s=%s' %(n,chr(n))), '\t', end = '\n')
            counter = 0
        else:
            print(('%s=%s' %(n,chr(n))), '\t', end = '')
# test2()


MENU_DICT = {
    1 : ['sprite', 5000],
    2 : ['rice', 20000],
    3 : ['fried chicken', 45000],
    4 : ['bulgogi', 78000],
    5 : ['water', 3000],
    6 : ['mandu', 35000],
    7 : ['curry and rice', 65000],
    8 : ['pork', 135000],
    9 : ['beef', 249500],
    10 : ['beer', 75000],
    }

line = """
------------------------------------------
"""
# print(type(MENU_DICT))
# print(MENU_DICT)
print(line)
print("""FUNXD's restaurant""")
print(line)
for n in range(1,11):
    # print('%-2s.%-17s.....%+7s won'%(n,MENU_DICT[n][0],MENU_DICT[n][1]),'\n')
    print('{:>2}.{:<17}..... {:>7,} won'.format(n,MENU_DICT[n][0],MENU_DICT[n][1]),'\n')
print(line)
