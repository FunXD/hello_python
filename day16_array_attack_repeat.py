"""
화일 독스트링 : 화일의 설명 - 가위.바위.보 -모듈(블랙박스)
"""
import os
import random
import time
import _script_run_utf8
_script_run_utf8.main()

VICTORY = 10  0
NUMBER_ATTACKS = 20
DECO_SEPARATOR = "=+" * 15
DRAW = ["-", "가위", "바위", "보ㅡ"]         # POS = 1,2,3 , POS'0'은 버린다.
RESULT = { 1: "승", 0: "패", -1 : "무"}    # 키값 = 1, 0, -1 로 호출한다.

def get_me_com_attacks(length=10):
    """ 가위.바위.보 - 랜덤어택 리스트 갯수'length'만큼을 생성한다.
    # 예: 3개 = [(1,2), (2,3), (1,1)] ... length=3
    """
    return [(random.randint(1, 3), random.randint(1,3)) for n in range(length)]

def get_result_rock_paper_scissors(me, com):
    """ 가위.바위.보 승무패를 판단해 준다.
    # IN = 1,2,3 중 하나, 가위,바위, 보 = me, com
    # OUT = 1,0,-1 중 하나 -- 승무패
    """
    eq = me - com
    if eq == 0:
        return -1       # ? = 무
    elif eq == 1 or eq == -2:
        return 1        # 1, Ture = 승
    elif eq == -1 or eq == 2:
        return 0        # 0, False = 패

def get_stack_win_draw_lose_count(judge, win_cnt, draw_cnt, lose_cnt):
    """ 모듈로 대체하는 구문 : 심판을 받아서, 승-무-패를 누적한다.
    # if judge == 1:
    #     win_count += 1
    # elif judge == 0:
    #     lose_count += 1
    # else:
    #     draw_count += 1
    """
    if judge == 1:
        win_cnt += 1
    elif judge == 0:
        lose_cnt += 1
    else:
        draw_cnt += 1
    return win_cnt, draw_cnt, lose_cnt

def is_stop_ok():
    return input("\n그만 하시겠습니까? (Yes/No=Enter)").lower().startswith("y")


percent = 0
fight_time = 0
# print(attacks)
while percent <=VICTORY:
    os.system('cls')
    attacks = get_me_com_attacks(NUMBER_ATTACKS)
    win_cnt, draw_cnt, lose_cnt = 0, 0, 0

    for i, attack in enumerate(attacks,1):
        judge = get_result_rock_paper_scissors(attack[0], attack[1])
        win_cnt, draw_cnt, lose_cnt = get_stack_win_draw_lose_count(judge, win_cnt, draw_cnt, lose_cnt)

        # print(attack, attack[0], attack[1], judge)

        print("{:2}".format(i), DRAW[attack[0]],'/', DRAW[attack[1]],'/', RESULT[judge])
    print(DECO_SEPARATOR)
    percent = (win_cnt/i*100)
    fight_time = fight_time+1
    print("{}승 {}무 {}패 {} 전 ----- 승률: {:.2f} % {}회 \n".format (
        win_cnt,
        draw_cnt,
        lose_cnt,
        i,
        percent,
        fight_time),flush=True)
    # if is_stop_ok():
    #     break
