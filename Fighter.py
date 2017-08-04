from Class import ClassLevels

class Fighter(ClassLevels):
    def __init__(self):
        self.HitDie = 10
        self.SkillPoints = 2
        self.ClassSkills = ['XC','XC','XC','Class','Class','XC','XC','XC','XC','XC','Class','XC','Class','XC','Class','Class','XC','XC','XC','XC','XC','XC','XC','XC','XC','XC','Class','Class','XC','XC','XC','XC','Class','Class','XC']
        self.SimpleWeaponProficiency = True
        self.MartialWeaponProficiency = True
        self.LightArmorProficiency = True
        self.MediumArmorProficiency = True
        self.HeavyArmorProficiency = True
        self.ShieldProficiency = True
        #added a leading zero to these BAB and saves list so that the # in the list corresponds to the level.
        self.BAB = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.FortSave = [0,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12]
        self.RefSave = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,]
        self.WillSave = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,]
