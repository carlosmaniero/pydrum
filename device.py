import usb.core
import usb.util
__all__ = ['Device']


class Device(object):
    '''Guitar Hero Drum device'''
    _id_vendor = 4794
    _id_product = 288
    _device = None
    _interface = 0
    _endpoint = None

    def get_id_vendor(self):
        return self._id_vendor

    def get_id_product(self):
        return self._id_product

    def get_device(self):
        '''Get device

        TODO: validate if device is conected and avaliable
        '''
        if not self._device:
            self._device = usb.core.find(
                idVendor=self.get_id_vendor(),
                idProduct=self.get_id_product()
            )

            if self._device.is_kernel_driver_active(self._interface):
                # tell the kernel to detach
                self._device.detach_kernel_driver(self._interface)
                # claim the device
                usb.util.claim_interface(self._device, self._interface)

        return self._device

    def get_endpoit(self):
        if not self._endpoint:
            dev = self.get_device()
            self._endpoint = dev[0][(0, 0)][0]
        return self._endpoint

    def read(self):
        dev = self.get_device()
        endpoint = self.get_endpoit()

        return dev.read(
            endpoint.bEndpointAddress,
            endpoint.wMaxPacketSize
        )
