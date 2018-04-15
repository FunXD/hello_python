""" 문제. A-1 편의점 물건을 계산하라
# 편의점 카운터에서 물건코드를 숫자(int)을 입력받은 후 최종가격을 알려주는 SW
# 가격DB는 3개만 딕셔너리 / 손님은 'item-갯수' 1-1 2-1 3-1 spc구분으로 입력
# 가장 심플한 영수증을 출력한다. (단, input구문은 테스트 CASE로 처리할 것!)
# input_str = input("번호-수량(공백)으로 입력 :")
# input_str = "1-1 2-2 3-1"
    빵ㅡ   : 1 x 1,000 = 1,000
    우유   : 4 x 2,000 = 8,000
    계란   : 1 x   500 =   500
    ------------ 합계: 9,500원
"""
import os
import sys

PRICE_DICT = {
    1: ("빵ㅡ", 1000),
    2: ("우유", 2000),
    3: ("계란", 500)}

DIRS = os.path.dirname(__file__).partition("hello_python\\")
ROOT = DIRS[0] + DIRS[1]
sys.path.append(ROOT)

import _script_run_utf8
_script_run_utf8.main()



# 아이템 번호-갯수,
input_data = "1-1 2-2 3-3"
print(PRICE_DICT[1][0])  # 빵
quit()
#---------------------------------------------

n=0
price = 0

order = input('어떤거?')

order_bill = order.strip().split('-')
_key = int(order_bill[0])
_value = int(order_bill[2])
price = (PRICE_DICT[_key][1]*_value)
print(price)
    # _key = int(order.strip().split('-')[0])
    # _value = int(order.strip().split('-')[1])


# if PRICE_DICT[0]
