class ClassLevels (object):
    def __init__(self):
        pass
    def getLevel(self):
        return self.Level
    def setLevel(self,Level):
        self.Level= Level
    def levelUp(self):
        self.Level = self.Level+1
    def getHitDie(self):
        return self.HitDie
    def getSkillPoints(self,IntMod):
        return self.Level*(self.SkillPoints+IntMod)
    def hasSimpleWeaponProficiency(self):
        return self.SimpleWeaponProficiency
    def hasMartialWeaponProficiency(self):
        return self.MartialWeaponProficiency
    def hasLightArmorProficiency(self):
        return self.LightArmorProficiency
    def hasMediumArmorProficiency(self):
        return self.MediumArmorProficiency
    def hasHeavyArmorProficiency(self):
        return self.HeavyArmorProficiency
    def hasShieldProficiency(self):
        return self.ShieldProficiency
    def getBAB(self):
        return self.BAB[self.getLevel()]
    def getFortSave(self):
        return self.FortSave[self.getLevel()]
    def getRefSave(self):
        return self.RefSave[self.getLevel()]
    def getWillSave(self):
        return self.WillSave[self.getLevel()]
    def getClassSkills(self):
        return self.ClassSkills

def chooseClass():
    classchoice = 99
    while classchoice>1:
        try:
            classchoice = int(input("Please choose your class: (1) Fighter."))
            if classchoice == 1:
                import Fighter
                Class = Fighter.Fighter()
            else:
                print("Please choose a valid, numerical option.")
        except ValueError:
            print("Sorry, that's not a valid option.")
    return Class
