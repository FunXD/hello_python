""" '피클'드 게시판 글쓰기
  - pickle.load(f) : 객체(f)를 읽어서 올린다.
  - pickle.dump(data, f) : 객체(f)에 데이터(data)를 덤프한다.
  - week_num = datetime.date(2018, 06, 12).weekday() : 요일
 """
import time
import datetime
import pickle
import os
import _script_run_utf8
_script_run_utf8.main()

FILENAME_WITH_DIR = "./_static/_pickle/pickled_dict.pck"

# BOARD_DICT = {
# 20180307:
# """ 3월 7일 뚜요일
# 오늘은 수학하건에 가따
# 노잼
# """,
#
# 20180308:
# """ 3월 8일 모교일
# 오늘도 수학하건에 가따
# 핵노잼
# """,
# 20180309:
# """ 3월 9일 그묘일
# 오늘은 그묘일! 내일운 쥬말이따
# 내일운 실껏 놀아야게따
# """,
#
# 20180310:
# """ 3월 10일 또요일
# 오눌 하건갓다가 개임을 햇따. 제미잇엇따
# """,
#
# 20180311:
# """ 3월 11일 이료일
# 오눌은 코딩을 밤에 해따
# 졸렷따
# """
#
#
# }


def write_pickle(filename_with_dir, data):
    with open(filename_with_dir, 'wb') as f:
        pickle.dump(data, f)

# write_pickle(FILENAME_WITH_DIR, BOARD_DICT)

def get_read_pickle(filename_with_dir):
    with open(FILENAME_WITH_DIR, 'rb')as f:
        return pickle.load(f)
get_read_pickle(FILENAME_WITH_DIR)


BOARD_DICT = get_read_pickle(FILENAME_WITH_DIR)
# print(list(BOARD_DICT.keys()))
# print(len(BOARD_DICT.keys()))


def show_board_list(board_list):
    print("중복데이터 : ('5건')")
    print("----------------------------------------------")
    print("번호....날짜......[제.....목]...............")
    print("----------------------------------------------")
    for i, key in enumerate(BOARD_DICT,1):
        title = BOARD_DICT[key].split('\n')[0]
        print ("%s. [%s] - %s"% (
            i,
            key,
            title
        ))
    print("----------------------------------------------")
    print(":입력 키값: (V)eiw / (A)dd / (Q)uit")
# show_board_list(BOARD_DICT)


def show_detail_view(board_dict,key):
    key_str = str(key)
    year, month, day = key_str[:4], key_str[4:6], key_str[6:]
    title = board_dict[key].split('\n')[0]
    content = board_dict[key].replace( title+'\n', ' ')

    print("%s (%s.%s.%s)" % (title, year, month, day))
    print("---------------------------------------------")
    print("%s" %content)
    print("---------------------------------------------")
    input("input = 엔터")
    os.system('cls')
    show_board_list(board_dict)
show_detail_view(BOARD_DICT,20180308)



BOARD_DICT = get_read_pickle(FILENAME_WITH_DIR)

while True:
    show_board_list(BOARD_DICT)
    order = input('명령을 입력하세요 v_날짜형식')
    if order[0].upper().startswith('v'):
        key + int(order.split('_'))
        show_detail_view(BOARD_DICT,key)
    elif order[0].upper().startswith('A'):
        pass
    elif order[0].upper().startswith('D'):
        pass
    elif order[0].upper().startswith('Q'):
        write_pickle(FILENAME_WITH_DIR, BOARD_DICT)
        quit
    else:
        print('명령어를 이해하지 못했습니다')
        os.system('cls')
        show_board_list(BOARD_DICT)
