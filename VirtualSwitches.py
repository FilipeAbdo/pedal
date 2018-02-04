from Tkinter import *

SwitchesWindow = Tk()
SwitchesWindow.title("Virtual Pedal")

# geometry syntax: WidthxHeight+Left+Top
SwitchesWindow.geometry("480x300+0+0")


def odPressed():
    print("OD Pressed")
    global odStatus
    if odStatus == True:
        odStatus = False
        od_lb.configure(background="green")
    else:
        odStatus = True
        od_lb.configure(bg="red")


def cmpPressed():
    print("CMP Pressed")
    global cmpStatus
    if cmpStatus == True:
        cmpStatus = False
        cmp_lb.configure(background="green")
    else:
        cmpStatus = True
        cmp_lb.configure(bg="red")


def delayPressed():
    print("Delay Pressed")
    global delayStatus
    if delayStatus == True:
        delayStatus = False
        delay_lb.configure(background="green")
    else:
        delayStatus = True
        delay_lb.configure(bg="red")


def reverbPressed():
    print("Reverb Pressed")
    global reverbStatus
    if reverbStatus == True:
        reverbStatus = False
        reverb_lb.configure(background="green")
    else:
        reverbStatus = True
        reverb_lb.configure(bg="red")


def fuzzPressed():
    print("FUZZ Pressed")
    global fuzzStatus
    if fuzzStatus == True:
        fuzzStatus = False
        fuzz_lb.configure(background="green")
    else:
        fuzzStatus = True
        fuzz_lb.configure(bg="red")


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
od_lb.place(x=lbStart+0*lbOffset, y=lbVPosition)
od_btn.place(x=bntStart, y=btnVPosition)
cmp_lb.place(x=lbStart + 1 * lbOffset, y=lbVPosition)
cmp_btn.place(x=bntStart + bntOffset, y=btnVPosition)
delay_lb.place(x=lbStart+2*lbOffset, y=lbVPosition)
delay_btn.place(x=bntStart + 2 * bntOffset, y=btnVPosition)
reverb_lb.place(x=lbStart+3*lbOffset, y=lbVPosition)
reverb_btn.place(x=bntStart + 3 * bntOffset, y=btnVPosition)
fuzz_lb.place(x=lbStart+4*lbOffset, y=lbVPosition)
fuzz_btn.place(x=bntStart + 4 * bntOffset, y=btnVPosition)

SwitchesWindow.mainloop()