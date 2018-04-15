import os
import sys

"""OOP.4 - 다형성 (폴리모피즘 : polymorphism)
----------------------------------------------
  모든 캐릭터의 베이스가 되는 클래스 Character()
   - self.val= hp, attack_power
   - self.func= attack, set demage, __str__
   - 모든 것의 정의(def)는 나중으로 미룬다.
"""

class player(Charactor):
    _total_count = 0

    def __init__(self):
        print("['%-12s'] 가 생성되었습니다.." % self.__class__.__name__)
        Character._total_count += 1
        self.hp = 0
        self.attack_power = 0

    def __str__(self):
        return "--- 이것은 ('%s')캐릭터 입니다 ---" %self.__class__.__name__

    def attack(self, other_obj):
        pass

    def set_demage(self, attack_power):       # 핼퍼()  ... attack()에서 사용.
        pass


DIRS = os.path.dirname(__file__).partition("hello_python")
ROOT = DIRS[0] + DIRS[1]
sys.path.append(ROOT)
sys.path.append(os.path.join(ROOT , "_static", "module_custom", ""))

from _1gc import Charactor
from _3gp import Player, Warrior, Magician
from _2gm import Monster, Firemonster, IceMonster


def status_obj_creation():
    print("\n\n")
    print("총 오브젝트=", Character._total_count)
    print("=========================")
    print("플레이어  =", Player._total_count)
    print("--------------")
    print(" 전 투 병 =", Warrior._total_count)
    print(" 마 법 사 =", Magician._total_count, "\n")

    print("몬스터괴물 =", Monster._total_count)
    print("--------------")
    print("  불꽃괴물 =", FireMonster._total_count)
    print("  얼음괴물 =", IceMonster._total_count)



if __name__ == '__main__':
    a = Warrior()
    b = Magician
    c = Firemonster
    d = IceMonster
    e = IceMonster

    status_obj_creation()
