import time
import usb.core
import usb.util


class DeviceConnection:

    def __init__(self):
        print("DeviceConnection created")
        self.idVendor = 0x0582
        self.idProduct = 0x01e5
        self.dev = []
        self.cfg = []
        self.intf = []
        self.ep_in = []
        self.ep_out = []
        self.connectionStatus = False

    #region Connection functions
    def connect(self):
            dev = usb.core.find(idVendor=self.idVendor, idProduct=self.idProduct)

            tries = 0

            if dev is None:
                    print "dev is None, entering to the while loop"
                    while dev is None:
                            print ("GT-001 wasn't found, pleas check USB connection! Try: " + str(tries))
                            time.sleep(0.5)
                            dev = usb.core.find(idVendor=self.idVendor, idProduct=self.idProduct)
                            tries += 1
                            if tries >= 10:
                                break;

            config_success = 0

            if dev is not None:
                tries = 0
            else:
                tries = 101

            while config_success == 0 and tries < 100:
                    try:
                            dev.set_configuration()
                            config_success = 1
                    except:
                            config_success = 0
                            print "Trying to configure device" +  str(tries)
                            tries += 1
                            time.sleep(0.1)

            if dev is not None:
                cfg = dev.get_active_configuration()
                intf = cfg[(3, 1)]
                usb.util.claim_interface(dev, intf)
                self.dev = dev
                self.cfg = cfg
                self.intf = intf

            self.connectionStatus = config_success

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