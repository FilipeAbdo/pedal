
class EffectsDict:

    def __init__(self):
        self.effectU003 = self.EffectU003()

    class Effect:

        def __init__(self, CCNumber, Value):
            self.CCNumber = CCNumber
            self.Value = Value

    class PedalBoard:

        def __init__(self):
            self.OD = EffectsDict.Effect(0x0B, 0x00)
            self.CMP = EffectsDict.Effect(0x0C, 0x00)
            self.Delay = EffectsDict.Effect(0x0D, 0x00)
            self.Reverb = EffectsDict.Effect(0x0E, 0x00)
            self.Fuzz = EffectsDict.Effect(0x0F, 0x00)

    class EffectU003:

        def __init__(self):
            self.EffectSetting = EffectsDict.PedalBoard()
            self.PatchNumber = 0x02