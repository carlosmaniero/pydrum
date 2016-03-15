import const
from device import Device

device = Device()
old = None
while True:
    try:
        data = device.read()
        if old != data:
            for index in const.BUTTONS:
                if data[index]:
                    print(const.BUTTONS_NAMES[index], data[index])
            old = data
            print('--' * 30)
    except KeyboardInterrupt:
        print('\nYou kill me')
        break
