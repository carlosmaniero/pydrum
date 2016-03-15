import usb.core

# Guitar Hero Drum device
# data 14/03/2016
# by ESpiga + Pomada

idVendor = 4794
idProduct = 288


dev = usb.core.find(
    idVendor=idVendor,
    idProduct=idProduct
)

interface = 0
endpoint = dev[0][(0, 0)][0]

YELLOW_INDEX = 11
ORANGE_INDEX = 16
RED_INDEX = 12
BLUE_INDEX = 14
GREEN_INDEX = 13
PEDAL_INDEX = 15

buttons = [
    YELLOW_INDEX,
    ORANGE_INDEX,
    RED_INDEX,
    BLUE_INDEX,
    GREEN_INDEX,
    PEDAL_INDEX
]

buttons_names = {}
buttons_names[YELLOW_INDEX] = 'YELLOW'
buttons_names[ORANGE_INDEX] = 'ORANGE'
buttons_names[RED_INDEX] = 'RED'
buttons_names[BLUE_INDEX] = 'BLUE'
buttons_names[GREEN_INDEX] = 'GREEN'
buttons_names[PEDAL_INDEX] = 'PEDAL'

if dev.is_kernel_driver_active(interface):
    # tell the kernel to detach
    dev.detach_kernel_driver(interface)
    # claim the device
    usb.util.claim_interface(dev, interface)

old = None
while True:
    try:
        try:
            data = dev.read(
                endpoint.bEndpointAddress,
                endpoint.wMaxPacketSize
            )
            if old != data:
                for index in buttons:
                    if data[index]:
                        print(buttons_names[index], data[index])
                old = data
                print('--' * 30)
        except usb.core.USBError as e:
            pass
    except KeyboardInterrupt:
        print('You kill me')
        break
