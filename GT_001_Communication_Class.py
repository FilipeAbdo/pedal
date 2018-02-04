import time
import usb.core
import usb.util


class DeviceConnection:

    def __init__(self):
        print("DeviceConnection created")
        self.dev = []
        self.cfg = []
        self.intf = []
        self.ep_in = []
        self.ep_out = []

    #region Connection functions
    def connect(self):
            dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)

            if dev is None:
                    print "dev is None, entering to the while loop"
                    while dev is None:
                            print "GT-001 wasn't found, pleas check USB connection!"
                            time.sleep(0.5)
                            dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)

            config_success = 0

            while config_success == 0:
                    try:
                            dev.set_configuration()
                            config_success = 1
                    except:
                            config_success = 0
                            print "Trying to configure device"
                            time.sleep(0.05)

            cfg = dev.get_active_configuration()
            intf = cfg[(3, 1)]
            usb.util.claim_interface(dev, intf)
            self.dev = dev
            self.cfg = cfg
            self.intf = intf

    def getEp_OUT(self):
            self.ep_out = usb.util.find_descriptor(
                    self.intf,
                    custom_match= \
                            lambda e: \
                                    usb.util.endpoint_direction(e.bEndpointAddress) == \
                                    usb.util.ENDPOINT_OUT)


    def getEp_IN(self):
            self.ep_in = usb.util.find_descriptor(
                    self.intf,
                    custom_match= \
                            lambda e: \
                                    usb.util.endpoint_direction(e.bEndpointAddress) == \
                                    usb.util.ENDPOINT_IN)

    #endregion

    #region Commmunication functions

    def writeCommand(self,command):
        self.ep_out.write(command)

    #endregion