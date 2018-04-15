
""" CAR INFORM """

FORM_INTRO = '''\
=================================
\tVEHICLE INFORMATION
---------------------------------
1. MODEL     : %s (%s)
2. MAX SPEED :      %d km/h
3. ACCELARAT :   +_ %d kmh
4. STATUS    :      %d kmh
---------------------------------\n\n\n'''


class Car(object):
    _total_count = 0
    _kind = ''
    _car_dict = dict()

    def __init__(self, arg_model):
        Car._total_count +=1
        Car._car_dict[Car._total_count] = [arg_model, self._kind]
        self.speed = 0
        print("['%-8s']!! A NEW CAR!! has come ... total: (%s)"%
                (arg_model, Car._total_count))
        self.attr = {
            'model' : arg_model,
            'kind' : self._kind,
            'max_speed' : 110,
            's_able' : 2,
            'speed' : self.speed
            }

    def show_status(self):
        args = tuple(self.attr.values())
        for item in Car._car_dict:
            print('\n\n', item)
        print(FORM_INTRO % args)

    def set_speed_up(self):
        if self.attr['speed'] + self.attr['s_able'] <= self.attr['max_speed']:
            self.attr['speed'] += self.attr['s_able']
            return True         # 정상가속
        else:
            self.attr['speed'] == self.attr['max_speed']
            return False        # 최고점 도달

    def set_speed_down(self):
        if self.attr['speed'] - self.attr['s_able'] <= self.attr['max_speed']:
            self.attr['speed'] -= self.attr['s_able']
            return True         # 감속해야하는데...
        else:
            self.sttr['speed'] == 0
            return False

    def say_speed(self, bool):
        if bool:
            print("PRESENT SPEED =", self.attr['speed'], "km/h")
        else:
            if self.attr['speed'] == 0:
                print(" ---- 차가 정지 했습니다. ----")
            else:
                print(" ---- 최고속도(%s km/h) 입니다. ----"%self.attr['max_speed'])

class SportCar(Car):
    _total_count = 0
    _kind = 'sports'

    def __init__(self, arg_model):
        super().__init__(arg_model)
        SportCar._total_count += 1
        self.attr = {
            'model':  arg_model,    # CAR NAME
            'kind':   self._kind,
            'max_speed':   110,     # MAXIMUM_SPEED
            's_able':   5,          # ACCELARATION
            'speed':   0,           # CURRENT SPEED
            }


class TruckCar(Car):
    _total_count = 0
    _kind = 'bongo'

    def __init__(self, arg_model):
        super().__init__(arg_model)
        TruckCar._total_count += 1
        self.attr = {
            'model':  arg_model,    # CAR NAME
            'kind':   self._kind,
            'max_speed':   500,     # MAXIMUM_SPEED
            's_able':   5,          # ACCELARATION
            'speed':   0,           # CURRNT SPEED
            }



if __name__ == '__main__':dya
    # print(FORM_INTRO %('Porsche','SportCar',300,20,0))

    a = SportCar('PORSCHE')
    b = TruckCar('poocar')
    def speed_up_down(obj):
        obj.show_status()

        while obj.attr['speed'] < obj.attr['max_speed']:
            obj.say_speed(obj.set_speed_up())

        obj.say_speed(obj.set_speed_up())

        while obj.attr['speed'] > 0:
            obj.say_speed(obj.set_speed_down())
        obj.say_speed(obj.set_speed_down())

    speed_up_down(a)
    speed_up_down(b)
