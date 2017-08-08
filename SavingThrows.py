#considering moving saving throws to Character
class SavingThrows (object):
    def __init__(self):
        pass
#        self.FortSaveTotal = FortSaveTotal
#        self.RefSaveTotal = RefSaveTotal
#        self.WillSaveTotal = WillSaveTotal
#        self.BaseFortSave = BaseFortSave
#        self.BaseRefSafe = BaseRefSave
#        self.BaseWillSave = BaseWillSave
    def calculate_saves(self,BaseFortSave,BaseRefSave,BaseWillSave,ConMod,DexMod,WisMod):
        self.FortSaveTotal = BaseFortSave+ConMod
        self.RefSaveTotal = BaseRefSave+DexMod
        self.WillSaveTotal=BaseWillSave+WisMod
    def get_fort_save(self):
        return self.FortSaveTotal
    def get_ref_save(self):
        return self.RefSaveTotal
    def get_will_save(self):
        return self.WillSaveTotal
    def display_saves(self):
        print("Fort: +", self.get_fort_save())
        print("Ref:  +", self.get_ref_save())
        print("Will: +", self.get_will_save())
