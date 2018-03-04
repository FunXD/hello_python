import _script_run_utf8
_script_run_utf8.main()

text1 = """피닉스 : 사망시각, 바로 지금. 사망원인, 바로 이몸이지, 뭐긴 뭐야!
스파크 : 스파크라 불러줘.난 치료하기도 하고 죽이기도 하지.아이러니한 모순이야. 뭐.. 그렇다고.
팬텀 : 사람들은 날 뒤에서 찌르는 야비한 새끼라고 부르지. 뭐, 네가 원한다면 앞에서도 찔러주지.
스토커 : 스토커라고 한다, 만나서 반가워.
프록시 : 당신은 제 지뢰에 가까이 오기는 커녕, 그 전에 굳 나잇이랍니다.
"""


text2 = "피닉스 : 사망시각, 바로 지금. 사망원인, 바로 이몸이지, 뭐긴 뭐야!\n" +\
        "스파크 : 스파크라 불러줘.난 치료하기도 하고 죽이기도 하지.아이러니한 모순이야. 뭐.. 그렇다고.\n" +\
        "팬텀 : 사람들은 날 뒤에서 찌르는 야비한 새끼라고 부르지. 뭐, 네가 원한다면 앞에서도 찔러주지.\n" +\
        "스토커 : 스토커라고 한다, 만나서 반가워.\n" +\
        "프록시 : 당신은 제 지뢰에 가까이 오기는 커녕, 그 전에 굳 나잇이랍니다.\n"


def write():
    """
    f=open('./_static/_pdb/day18-1_text.pdb','w',encoding='utf8')
    f.write(text2)
    f.close
    """

    with open('./_static/_pdb/day18-1_text.pdb','w',encoding='utf8') as f:
        f.write(text1)

    with open('./_static/_pdb/day18-1_text.pdb','a',encoding='utf8') as f:
        f.write(text2)


write()
