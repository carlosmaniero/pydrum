import const
from device import Device
from drum import Crash, Snare, HiHat, Bass, HiTom, LowTom, Cymbal

crash = Crash()
snare = Snare()
hihat = HiHat()
bass = Bass()
hi_tom = HiTom()
low_tom = LowTom()
cymbal = Cymbal()

device = Device()
old = None
while True:
    try:
        data = device.read()
        if old != data:
            for index in const.BUTTONS:
                if data[index]:
                    if index == const.RED_INDEX:
                        snare.shot(data[index])
                    elif index == const.YELLOW_INDEX:
                        hihat.shot(data[index])
                    elif index == const.PEDAL_INDEX:
                        bass.shot(data[index])
                    elif index == const.BLUE_INDEX:
                        low_tom.shot(data[index])
                    elif index == const.GREEN_INDEX:
                        hi_tom.shot(data[index])
                    elif index == const.ORANGE_INDEX:
                        cymbal.shot(data[index])
                    print(const.BUTTONS_NAMES[index], data[index])
            old = data
            print('--' * 30)
    except KeyboardInterrupt:
        print('\nYou kill me')
        break
