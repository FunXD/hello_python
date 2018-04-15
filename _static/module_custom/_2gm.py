from _1gc import *



class Monster(Charactor):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Monster._total_count +=1

class FireMonster(Monster):
    _total_count = 0

    def __init__(self):
        super().__init__()
        FireMonster._total_count +=1
        print("%s 생성되었습니다."% self.__class__.__name__)

class IceMonster(Monster):
    _total_count = 0

    def __init__(self):
        super().__init__()
        IceMonster._total_count +=1
        print("['%s']")



if __name__ == '__main__':
    a = Monster()
    b = Monster()

    print("캐릭터의 갯수=", Charactor._total_count)
    print("몬스터의 갯수=", Monster._total_count)
