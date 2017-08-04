import Stats
class SavingThrows (object):
    def __init__(self):
        pass
#        self.FortSaveTotal = FortSaveTotal
#        self.RefSaveTotal = RefSaveTotal
#        self.WillSaveTotal = WillSaveTotal
#        self.BaseFortSave = BaseFortSave
#        self.BaseRefSafe = BaseRefSave
#        self.BaseWillSave = BaseWillSave
    def CalculateSaves(self,BaseFortSave,BaseRefSave,BaseWillSave,ConMod,DexMod,WisMod):
        self.FortSaveTotal = BaseFortSave+ConMod
        self.RefSaveTotal = BaseRefSave+DexMod
        self.WillSaveTotal=BaseWillSave+WisMod
    def getFortSave(self):
        return self.FortSaveTotal
    def getRefSave(self):
        return self.RefSaveTotal
    def getWillSave(self):
        return self.WillSaveTotal
    def displaySaves(self):
        print("Fort: +", self.getFortSave())
        print("Ref:  +", self.getRefSave())
        print("Will: +", self.getWillSave())
