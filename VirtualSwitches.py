from Tkinter import *
from GT_001_Communication_Class import *
from EffectsManager import *
from CommandsManager import *

SwitchesWindow = Tk()
SwitchesWindow.title("Virtual Pedal")

# geometry syntax: WidthxHeight+Left+Top
SwitchesWindow.geometry("480x300+0+0")
connection = DeviceConnection()
effectsManager = EffectsDict()
commandManager = CommandsManager()

def odPressed():
    print("OD Pressed")
    global odStatus
    if odStatus:
        odStatus = False
        od_lb.configure(background="green")
        effectsManager.effectU003.EffectSetting.OD.Value = 0x7F
    else:
        odStatus = True
        od_lb.configure(bg="red")
        effectsManager.effectU003.EffectSetting.OD.Value = 0x00

    connection.writeCommand(commandManager.getCC_Command(effectsManager.effectU003.EffectSetting.OD.CCNumber,
                                                         effectsManager.effectU003.EffectSetting.OD.Value))


def cmpPressed():
    print("CMP Pressed")
    global cmpStatus
    if cmpStatus:
        cmpStatus = False
        cmp_lb.configure(background="green")
    else:
        cmpStatus = True
        cmp_lb.configure(bg="red")


def delayPressed():
    print("Delay Pressed")
    global delayStatus
    if delayStatus:
        delayStatus = False
        delay_lb.configure(background="green")
    else:
        delayStatus = True
        delay_lb.configure(bg="red")


def reverbPressed():
    print("Reverb Pressed")
    global reverbStatus
    if reverbStatus:
        reverbStatus = False
        reverb_lb.configure(background="green")
    else:
        reverbStatus = True
        reverb_lb.configure(bg="red")


def fuzzPressed():
    print("FUZZ Pressed")
    global fuzzStatus
    if fuzzStatus:
        fuzzStatus = False
        fuzz_lb.configure(background="green")
    else:
        fuzzStatus = True
        fuzz_lb.configure(bg="red")


def connectPressed():
    print("Connection Requested")
    connection.connect()
    if connection.connectionStatus:
        connectionStatus_val["text"] = "Connected"
        connectionStatus_val["bg"] = "Green"
    else:
        connectionStatus_val["text"] = "Connection Fail"
        connectionStatus_val["bg"] = "red"


odStatus = False
cmpStatus = False
delayStatus = False
reverbStatus = False
fuzzStatus = False


od_lb = Label(SwitchesWindow,width=2,background="green")
cmp_lb = Label(SwitchesWindow,width=2,background="green")
delay_lb = Label(SwitchesWindow,width=2,background="green")
reverb_lb = Label(SwitchesWindow,width=2,background="green")
fuzz_lb = Label(SwitchesWindow,width=2,background="green")


od_btn = Button(SwitchesWindow, text="OD", width=6, command=odPressed)
cmp_btn = Button(SwitchesWindow, text="CMP", width=6,command=cmpPressed)
delay_btn = Button(SwitchesWindow, text="Delay", width=6, command=delayPressed)
reverb_btn = Button(SwitchesWindow, text="Reverb", width=6, command=reverbPressed)
fuzz_btn = Button(SwitchesWindow, text="FUZZ", width=6, command=fuzzPressed)

bntOffset = 480/5
bntStart = 10
btnVPosition = 122
lbStart = bntStart + 30
lbOffset = bntOffset
lbVPosition = 95
# od_lb.place(x=lbStart+0*lbOffset, y=lbVPosition)
# od_btn.place(x=bntStart, y=btnVPosition)
# cmp_lb.place(x=lbStart + 1 * lbOffset, y=lbVPosition)
# cmp_btn.place(x=bntStart + bntOffset, y=btnVPosition)
# delay_lb.place(x=lbStart+2*lbOffset, y=lbVPosition)
# delay_btn.place(x=bntStart + 2 * bntOffset, y=btnVPosition)
# reverb_lb.place(x=lbStart+3*lbOffset, y=lbVPosition)
# reverb_btn.place(x=bntStart + 3 * bntOffset, y=btnVPosition)
# fuzz_lb.place(x=lbStart+4*lbOffset, y=lbVPosition)
# fuzz_btn.place(x=bntStart + 4 * bntOffset, y=btnVPosition)
od_lb.grid(row=2, column=0)
od_btn.grid(row=3, column=0)
cmp_lb.grid(row=2, column=1)
cmp_btn.grid(row=3, column=1)
delay_lb.grid(row=2, column=2)
delay_btn.grid(row=3, column=2)
reverb_lb.grid(row=2, column=3)
reverb_btn.grid(row=3, column=3)
fuzz_lb.grid(row=2, column=4)
fuzz_btn.grid(row=3, column=4)

space_lb = Label(SwitchesWindow,height=5)
space_lb.grid(row=1, column=0)

connect_btn = Button(SwitchesWindow,text="Connect to GT-001", width=25, command=connectPressed)
connectionStatus_lb = Label(SwitchesWindow, text="Status: ", width=15)
connectionStatus_val = Label(SwitchesWindow, text="Idle", font="Arial 10 bold", width=23, bg="yellow")

connect_btn.grid(row=0, column=0, columnspan=2, sticky=W+E) #pack(side=LEFT, anchor=N, expand=TRUE) #place(x=10, y=10)
connectionStatus_lb.grid(row=0, column=2, sticky=W+E) #.pack(side=LEFT, anchor=N, expand=TRUE)#place(x=200, y=10)
connectionStatus_val.grid(row=0, column=3, columnspan=2, sticky=W+E) #.pack(side=LEFT, anchor=N, expand=TRUE)#place(x=250, y=10)

SwitchesWindow.mainloop()