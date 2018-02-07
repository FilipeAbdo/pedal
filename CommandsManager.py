from EffectsManager import *

class CommandsManager:
    def __init__(self):
        self.CCCommand = [0x2B, 0xB0, 0x00, 0x00]  # 0x2B, 0xB0, CC#n (Change Control Number) , VV (Value)
        self.PC_Command = [0x2C, 0xC0, 0x00, 0x00]  # 0x2B, 0xB0, CC#n (Change Control Number) , VV (Value)

    def getCC_Command(self, efect):
        assert isinstance(EffectsDict, efect)
        command = self.CCCommand

        command[2] = efect.CCNumber
        command[3] = efect.Value

        return command

    def getPC_Command(self, patchNumber):

        command = self.PC_Command

        command[2] = patchNumber

        return command