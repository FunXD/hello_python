""" 문제. winsound 모듈의 beep() 메서드를 이용해서 소리를 내라
 - 미션.1 = beep() 메서드의 인자(파라미터)를 알아내라
 - 미션.2 = 37에서 200에 +50씩 증가하면서 소리를 낸다.
 - 미션.3 = 소리를 낼때마다, "n번째 발성을 하였습니다. 파라미터는 (무엇)입니다."
"""

import winsound
import time
# frequency = 37
# duration = 200
# for n in range (20):
#     winsound.Beep(frequency, duration)
#     frequency = frequency+50
#     duration = duration+50
#     print(n,'번째 발성을 하였습니다.','\n','파라메터는',frequency,'입니다','\n')


scale = {'C':(65.406, 130.81, 261.63, 523.25, 1046.5, 2093.0),
         'C#':(69.296, 138.59, 277.18, 554.37, 1108.7, 2217.5),
         'D':(73.416, 146.83, 293.67, 587.33, 1174.7, 2349.3),
         'D#':(77.782, 155.56, 311.13, 622.25, 1244.5, 2489.0),
         'E':(82.407, 164.81, 329.63, 659.26, 1318.5, 2637.0),
         'F':(87.307, 174.61, 349.23, 698.46, 1396.9, 2793.0),
         'F#':(92.499, 185.00, 369.99, 739.99, 1480.0, 2960.0),
         'G':(97.999, 196.00, 392.00, 783.99, 1568.0, 3136.0),
         'G#':(103.83, 207.65, 415.30, 830.61, 1661.2, 3322.4),
         'A':(110.00, 220.00, 440.00, 880.00, 1760.00, 3520.0),
         'A#':(116.54, 233.08, 466.16, 932.33, 1864.7, 3729.3),
         'B':(123.47, 246.94, 493.88, 987.77, 1975.5, 3951.1)}


def play_notes(fast):
    if (notes[a]) ==1:
        winsound.Beep(261,fast)
    if (notes[a]) ==2:
        winsound.Beep(293,fast)
    if (notes[a]) ==3:
        winsound.Beep(329,fast)
    if (notes[a]) ==4:
        winsound.Beep(349,fast)
    if (notes[a]) ==5:
        winsound.Beep(391,fast)
    if (notes[a]) ==6:
        winsound.Beep(440,fast)
    if (notes[a]) ==7:
        winsound.Beep(493,fast)
    if (notes[a]) ==8:
        winsound.Beep(520,fast)
    if (notes[a]) ==0:
        time.sleep(0.5)



speed = int(input('속도는?'))
notes = []
times=(int(input('몇번 할까요?')))
print("\n")
for n in range(times):
    choice = (int(input('1~8중 하나를 선택하십시오(0은 쉬기)')))
    notes.append(choice)
print (notes)
a=0
for n in range(times):
    play_notes(speed)
    a=a+1





def plays_notes(notes,delay):
    for note in notes:
        win.Beep(dict[note],delay)
