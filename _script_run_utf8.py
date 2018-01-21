"""
  (1) PATH. OS, sys
  (2) Encoding : Slide Share =
  (3) encoding - decoding
  (4) enumerate, zip, map, lambda

 Understanding UNICODE & encoding UTF-8
  - it only can work in 'Console' <f5>,
    not in script-run <shift+ctrl+B>
    for detail : published 2016.3/2 - understanding UNICODE
        https://www.slideshare.net/dahlmoon/string-20160310 = lv5
        https://www.slideshare.net/JaehoonJung/ss-49316384?next_slideshow=2

    for Korean-'Hangul' : https://libsora.so/posts/python-hangul/

    also refer here: Unicode FileFormat.Info:
        http://www.fileformat.info/info/unicode/char/0180/index.htm
 """
import os
import sys
import time

def test1_path_control():
    _a = os.path.dirname(__file__)
    print('_a = %s'%_a)

    _b = os.path.dirname(os.path.dirname(__file__))
    print('_b = %s'%_b)

    _c = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print('_c = %s'%_c)

    _d = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    print('_d = %s'%_d)


    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    for path in sys.path:
        print(path)
# test1_path_control()

import _script_run_utf8
_script_run_utf8.main()

def test2_unicode_utf8_test():
    print(sys.getdefaultencoding())
    print(sys.stdout.encoding)
    print(sys.stderr.encoding)
    print('안녕세계 --> Hello World')
# test2_unicode_utf8_test()

def test3_ascii_unicode(start, end):
    """
    U+0000 ~ U+007F = 128자 / Basic Latin
    U+0080 ~ U+00FF = 128자 / Latin-1 Supplement
    U+ac00 ~ U+d7af = 11184자 / Hangul sylables
    http://www.fileformat.info/info/unicode/char/0180/index.htm
    """
    column = 0
    for n in range(start, end):
        column += 1

        if n in [7, 8, 9, 10, 13,]:
            letter = '?'
        else:
            letter = chr(n)

        if column < 6:
            print('{:3}={}  '.format(n, letter), end='')
        else:
            column = 0
            print('{:3}={}  '.format(n, letter), end='\n')
# test3_ascii_unicode(0xac00, 0xacff)
# test3_ascii_unicode(0x00, 0x7f)
# test3_ascii_unicode(0x80, 0xff)

def test4_unicode_encoding():
    import unicodedata
    num = 0xac00        # 44032
    uni = '\uAC00'      # '가'

    print('\\uAC00 = %s'% uni)
    print('chr(0xac00) = %s'% chr(num))
    print(unicodedata.name(uni), end='\n\n')

    print('\\uac00.encode(encoding=\'utf8\') = %s'
        % '\uac00'.encode(encoding='utf_8'))
    print('b\\xea\\xb0\\x80.decode(encoding=\'utf8\') = %s'
        % b'\xea\xb0\x80'.decode(encoding='utf8'), end='\n\n')

    print('\\uac00.encode(encoding=\'utf_16\') = %s'
        % '\uac00'.encode(encoding='utf_16'))
    print('b\\xff\\xfe\\x00\\xac.decode(encoding=\'utf_16\') = %s'
        % b'\xff\xfe\x00\xac'.decode(encoding='utf_16'), end='\n\n')

    print('\\uac00.encode(encoding=\'cp949\') = %s'
        % '\uac00'.encode(encoding='cp949'))
    print('b\\xb0\\xa1.decode(encoding=\'utf_16\') = %s'
        % b'\xb0\xa1'.decode(encoding='cp949'), end='\n\n')
# test4_unicode_encoding()

def test5_show_flushing():
    while True:
        for n in range(10):
            print(n, end='')
            sys.stdout.flush()
            time.sleep(0.4)
            # print('\a',end='')
        time.sleep(3)
        os.system('cls')
# test5_show_flushing()

def test6_zip_obj():
    _year = '갑을병정무기경신임계'
    _number = '4567890123'
    _zodiac = '자축인묘진사오미신유술해'

    _a = zip(_number, _year)
    print(_a)           # <zip object at 0x02517CD8>
    print(list(_a))

    _a = zip(_number, _year)
    print(tuple(_a))

    _a = zip(_number, _year)
    print(set(_a))

    _a = zip(_number, _year)
    print(dict(_a))
# test6_zip_obj()

def test7_lambda():
    # _a = (lambda x: x**2)(3)
    # print(_a)      # 3**2 = 9
    #
    # _b = (lambda x,y: x**2 + y**2)(3,2)
    # print(_b)     # 3**2 + 2**2 = 9+4= 13

    def func_01(x):
        print(x**2)

    def func_02(x,y):
        print(x**2 + y**2)

    func_01(3)      # 3**2 = 9
    func_02(3,2)    # 3**2 + 2**2 = 9+4= 13
# test7_lambda()

def test8_map_zip():
    def func_01(x,y):
        print(x**2 + y**2)

    x_arr = [2,4,6,8,10]
    y_arr = [1,3,5,7,9]

    _a = zip(x_arr, y_arr)
    print(list(_a))

    _b = map(func_01, x_arr, y_arr)
    # _b = map(lambda x,y: x**2+y**2, x_arr, y_arr)
    print(_b)       # <map object at 0x024DC4F0>
    print(list(_b))
# test8_map_zip()



def main_year_zodiac(target_year):
    """ calculate year zodiac
    : http://blog.naver.com/PostView.nhn?blogId=kdjzzang310&logNo=220578616822
      - 갑: 甲 (갑옷갑): 큰나무, 한번 쓰러지면 재기하기 어렵다.
      - 을: 乙 (새을): 새싹, 생명력이 강하다.
      - 병: 丙 (밝을병): 태양
      - 정: 丁 (넷째 천간병): 쇠를 녹이는 불, 촛불, 등대
      - 무: 戊 (다섯째 천간무): 큰산
      - 기: 己 (자기기): 논, 밭, 기름진 땅, 농사를 지을 수 있는 땅
      - 경: 庚 (일곱째 천간경): 사람손길이 필요한 다듬어지지 않은 원석,바위,쇳덩어리
      - 신: 辛 (매울신): 사람손길로 다듬어진 쇠붙이, 바늘, 칼, 못, 침, 보석, 장신구
      - 임: 壬 (북방임): 큰바다, 거대한 호수
      - 계: 癸 (열째천간계): 작은 시냇물, 샘물, 서리

      - 갑,을 (청색) = 목(木)
      - 병,정 (적색) = 화(火)
      - 무,기 (황색) = 토(土)
      - 경,신 (백색) = 금(金)
      - 임,계 (흑색) = 수(水)
    """
    import _script_run_utf8
    _script_run_utf8.main()

    base_year = 2008        # 무자년(쥐띠해) = 2008년
    target_year = target_year      # 임진년(용띠해) = 1592년
    _answer = base_year - target_year         # 421
    _year = '갑을병정무기경신임계'              # 10
    _number = '4567890123'
    _zodiac = '자축인묘진사오미신유술해'        # 12

    gap = dict(zip(_number, _year))

    print(_zodiac + str(_answer))      # 421
    print(gap)          # show dict

    # print(len(_year))
    # print(len(_zodiac))

    _f = _answer%12         # rest = 1
    _g = _answer//12        # value = 35
    # print('_answer %% 12 = %s : go backward'%_f)   # 1

    _key_gap = str(target_year)[-1]
    _key_zod = 12-_f

    if _key_zod == 12:
        _key_zod = 0

    print('\n{}{}년 ({}) \n\n\n'.format(
            gap[_key_gap],
            _zodiac[_key_zod],
            target_year)
        )

if __name__ == '__main__':
    main_year_zodiac(1592)      # 임진년 - 검은 용
    main_year_zodiac(2000)      # 경진년 - 하얀 용
    main_year_zodiac(2004)      # 갑신년 - 파란 원숭이
    main_year_zodiac(2016)      # 병신년 - 붉은 원숭이
    main_year_zodiac(2017)      # 정유년 - 붉은 닭
