import Adafruit_BBIO.GPIO as GPIO
import time
import usb.core
import usb.util


#region Functions Definitions

def connect():
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

        return intf;

def getEp_OUT(intf):
        ep_out = usb.util.find_descriptor(
                intf,
                custom_match= \
                        lambda e: \
                                usb.util.endpoint_direction(e.bEndpointAddress) == \
                                usb.util.ENDPOINT_OUT)
        return ep_out;


def getEp_IN(intf):
        ep_in = usb.util.find_descriptor(
                intf,
                custom_match= \
                        lambda e: \
                                usb.util.endpoint_direction(e.bEndpointAddress) == \
                                usb.util.ENDPOINT_IN)
        return ep_in;

#endregion


#region Input Configurations
IO_PIN1 = "P8_12"
IO_PIN2 = "P8_14"
IO_PIN3 = "P8_16"
IO_PIN4 = "P8_18"

LED_PIN1 = "P8_17"
LED_PIN2 = "P8_15"
LED_PIN3 = "P8_11"
LED_PIN4 = "P8_9"


GPIO.setup(IO_PIN1,GPIO.IN)
GPIO.setup(IO_PIN2,GPIO.IN)
GPIO.setup(IO_PIN3,GPIO.IN)
GPIO.setup(IO_PIN4,GPIO.IN)

GPIO.setup(LED_PIN1,GPIO.OUT)

GPIO.add_event_detect(IO_PIN1, GPIO.RISING)
GPIO.add_event_detect(IO_PIN2, GPIO.RISING)
GPIO.add_event_detect(IO_PIN3, GPIO.RISING)
GPIO.add_event_detect(IO_PIN4, GPIO.RISING)

in1_event_detected = 0
in2_event_detected = 0
in3_event_detected = 0
in4_event_detected = 0
#endregion

#region GT-001 parameters configuration
idVendor = 0x0582
idProduct = 0x01e5

#The last position of CCxx command shall be 0:False or 127:True (0x7F)
CC11_Command = [0x2B, 0xB0, 0x0B, 0x00]  #OD Control
CC12_Command = [0x2B, 0xB0, 0x0C, 0x00]  #CMP Control
CC13_Command = [0x2B, 0xB0, 0x0D, 0x00]  #Delay Control
CC14_Command = [0x2B, 0xB0, 0x0E, 0x00]  #Reverb Control

#endregion

#region connect to GT-001

# dev = usb.core.find(idVendor=idVendor,idProduct=idProduct)
#
# if dev is None:
#         print "dev is None, entering to the while loop"
#         while dev is None:
#                 print "GT-001 wasn't found, pleas check USB connection!"
#                 time.sleep(0.5)
#                 dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)
#
# config_success = 0
#
# while config_success == 0:
#         try:
#                 dev.set_configuration()
#                 config_success = 1
#         except:
#                 config_success = 0
#                 print "Trying to configure device"
#                 time.sleep(0.05)


# cfg = dev.get_active_configuration()
# intf = cfg[(3,1)]
# usb.util.claim_interface(dev,intf)

intf = connect()


# ep_out = usb.util.find_descriptor(
#     intf,
#     custom_match = \
#         lambda e: \
#         usb.util.endpoint_direction(e.bEndpointAddress) == \
#         usb.util.ENDPOINT_OUT)
#
# ep_in = usb.util.find_descriptor(
#     intf,
#     custom_match = \
#         lambda e: \
#         usb.util.endpoint_direction(e.bEndpointAddress) == \
#         usb.util.ENDPOINT_IN)

ep_out = getEp_OUT(intf)

ep_in = getEp_IN(intf)

assert ep_in is not None
assert ep_out is not None
print  "ep_in End Point Address = " + str(ep_in.bEndpointAddress)

#region reset configuration

ep_out.write(CC11_Command)
time.sleep(0.05)
ep_out.write(CC12_Command)
time.sleep(0.05)
ep_out.write(CC13_Command)
time.sleep(0.05)
ep_out.write(CC14_Command)
time.sleep(0.05)

#endregion

#endregion

while True:
        #region Input 1 Solution
        Input1 = GPIO.input(IO_PIN1)
        if GPIO.event_detected(IO_PIN1):
                print "event detected!"
                in1_pressed_time = 0
                in1_event_detected = 1

        if Input1:
                if in1_pressed_time >= 50 and in1_event_detected:
                        print "Input 1 Ack!!! Pressed_Time =  " + str(in1_pressed_time) + " Event Detection = " + str(in1_event_detected)

                        if CC11_Command[3] == 0:
                                print "Sent ON to CC11"
                                CC11_Command[3] = 0x7F
                                GPIO.output(LED_PIN1,GPIO.HIGH)
                        else:
                                print "Sent OFF to CC11"
                                CC11_Command[3] = 0x00
                                GPIO.output(LED_PIN1, GPIO.LOW)
                        try:
                                ep_out.write(CC11_Command)
                        except usb.core.USBError as e:
                                print "Error writing OD command \n"
                                intf = connect()
                                ep_out = getEp_OUT(intf)
                                ep_out.write(CC11_Command)

                        in1_event_detected = 0
                else:
                        in1_pressed_time += 1
        #endregion

        #region Input 2 Solution
        Input2 = GPIO.input(IO_PIN2)
        if GPIO.event_detected(IO_PIN2):
                print "event detected!"
                in2_pressed_time = 0
                in2_event_detected = 1

        if Input2:
                if in2_pressed_time >= 50 and in2_event_detected:
                        print "Input 2 Ack!!! Pressed_Time =  " + str(in2_pressed_time) + " Event Detection = " + str(in2_event_detected)

                        if CC12_Command[3] == 0:
                                print "Sent ON to CC12"
                                CC12_Command[3] = 0x7F
                        else:
                                print "Sent OFF to CC12"
                                CC12_Command[3] = 0x00

                        try:
                                ep_out.write(CC12_Command)
                        except usb.core.USBError as e:
                                print "Error writing CMP command \n"
                                intf = connect()
                                ep_out = getEp_OUT(intf)
                                ep_out.write(CC12_Command)

                        in2_event_detected = 0
                else:
                        in2_pressed_time += 1

        # endregion

        # region Input 3 Solution
        Input3 = GPIO.input(IO_PIN3)
        if GPIO.event_detected(IO_PIN3):
                print "event detected!"
                in3_pressed_time = 0
                in3_event_detected = 1

        if Input3:
                if in3_pressed_time >= 50 and in3_event_detected:
                        print "Input 3 Ack!!! Pressed_Time =  " + str(
                                in3_pressed_time) + " Event Detection = " + str(in3_event_detected)

                        if CC13_Command[3] == 0:
                                print "Sent ON to CC13"
                                CC13_Command[3] = 0x7F
                        else:
                                print "Sent OFF to CC13"
                                CC13_Command[3] = 0x00

                        try:
                                ep_out.write(CC13_Command)
                        except usb.core.USBError as e:
                                print "Error writing DELAY command \n"
                                intf = connect()
                                ep_out = getEp_OUT(intf)
                                ep_out.write(CC13_Command)

                        in3_event_detected = 0
                else:
                        in3_pressed_time += 1

        # endregion

        # region Input 4 Solution
        Input4 = GPIO.input(IO_PIN4)
        if GPIO.event_detected(IO_PIN4):
                print "event detected!"
                in4_pressed_time = 0
                in4_event_detected = 1

        if Input4:
                if in4_pressed_time >= 50 and in4_event_detected:
                        print "Input 4 Ack!!! Pressed_Time =  " + str(
                                in4_pressed_time) + " Event Detection = " + str(in4_event_detected)

                        if CC14_Command[3] == 0:
                                print "Sent ON to CC14"
                                CC14_Command[3] = 0x7F
                        else:
                                print "Sent OFF to CC14"
                                CC14_Command[3] = 0x00

                        try:
                                ep_out.write(CC14_Command)
                        except usb.core.USBError as e:
                                print "Error writing REVERB command \n"
                                intf = connect()
                                ep_out = getEp_OUT(intf)
                                ep_out.write(CC14_Command)

                        in4_event_detected = 0
                else:
                        in4_pressed_time += 1

        # endregion

        time.sleep(0.001)

exit(0)
