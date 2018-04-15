import os
import sys
import datetime
""" file-docs : OPEN A RESTAURANT : Making Order System
  (1) to Show MENU_PAN = MENU_PAN (changeable)
  (2) to Input order = by Item index & quantity
  (3) to Calculate the Bills = Including (Tax= 6.5%, Tip= 10%)

 * Release Note : correct sorting version
    - Dict can not be ordered / arrange 'list' first.
    - Question : _arr.sort() = None. sorted(_arr) = 'list' O.K
    - I don't know the differences btw .sort() & sorted()
"""
SEPARATOR = '__'*22
MENU_DICT = {
    1 : ['POLLUTED_WATER', 1500],
    2 : ['DIRTY_WATER', 2000],
    3 : ['WATER', 4000],
    4 : ['HOT_WATER', 6000],
    5 : ['COLD_WATER', 6000],
    6 : ['ICE_WATER', 7000],
    7 : ['MINERAL_WATER', 8500],
    8 : ['ENERGY_WATER', 10000],
    9 : ['MEDICINE_WATER', 25000],}
MENU_PAN_FORMAT = ""                                +\
    "-------------------------------------------\n" +\
    "     MENU-PAN  / FunXD's Restaurant        \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"
BILL_FORMAT = ""                                    +\
    "-------------------------------------------\n" +\
    "     $$$ BILL / FunXD's Restaurant $$$     \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"

def show_menu_pan():
    """ MAKING MENU_PAN of Your RESTAURANT
      - print(MENU_PAN_FORMAT % MENU_STRING)
      - make MENU_STRING from MENU_DICT
    """
    MENU_STRING = ''
    for key in MENU_DICT.keys():            # use .keys() .values() .items()
        MENU_STRING += '{:>2}. {:<16} {:.^10} {:6,} won'.format(
            key,
            MENU_DICT[key][0],
            '.',
            MENU_DICT[key][1]) + '\n'
    print(MENU_PAN_FORMAT %MENU_STRING)
show_menu_pan()


# def get_input_str():
#     input_message = ''+\
#         'Please order menu by index-quantity & space\n'+\
#         'Ex) 1-2 2-1 3-2... just once for each index\n'
#
#     menu_order_str = input(input_message)
#     return menu_order_str

input_message = ''+\
    'Please order menu by index-quantity & space\n'+\
    'Ex) 1-2 2-1 3-2... just once for each index\n'
print(input_message)
# menu_order_str = get_nput_str()
menu_order_str=input('Your Order = ')


# print(menu_order_str)
# print(type(menu_order_str))

order_arr = menu_order_str.strip().split()

# print(order_arr[0])
# print(order_arr[1])
# print(order_arr[2])

_a_arr = order_arr[0].strip().split('-')
# print(_a_arr)
#
#
# print(_a_arr[0])
# print(_a_arr[1])
#
ORDER_DICT = {}
#
#
# _key = _a_arr[0]
# _value = _a_arr[1]
#
# ORDER_DICT[_key] = _value
# print(ORDER_DICT)

for order in order_arr:
    _key = int(order.strip().split('-')[0])
    _value = int(order.strip().split('-')[1])
    ORDER_DICT[_key] = _value
print(ORDER_DICT, end='\n\n\n')

menu_total = 0

for i, key in enumerate(ORDER_DICT.keys(), 5):
    _item = MENU_DICT[key][0]
    _price = MENU_DICT[key][1]
    _quantity = ORDER_DICT[key]
    _total = _price * _quantity
    menu_total += _total
    print('{:2}.{:<15} {:.^10} {:6,} x{:2} = {:7,}won'.format(i,_item,'.',_price,_quantity,_total))
print('{:7,}'.format(menu_total))
print(SEPARATOR)
print('\t\t\t\t\t   {:7,} won'.format(menu_total))
