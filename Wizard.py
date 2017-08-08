from Class import ClassLevels

class Wizard(ClassLevels):
    def __init__(self):
        self.HitDie = 6
        self.SkillPoints = 2
        self.ClassSkills = ['XC','Class','XC','XC','Class','XC','XC','XC','XC','Class','XC','XC','XC','Class','Class','Class','Class','Class','Class','Class','Class','Class','Class','Class','XC','XC','Class','XC','XC','XC','Class','XC','XC','XC','XC']
        #need to add specific weapon proficiencies for club, quarterstaff, etc.
        self.SimpleWeaponProficiency = False
        self.MartialWeaponProficiency = False
        self.LightArmorProficiency = False
        self.MediumArmorProficiency = False
        self.HeavyArmorProficiency = False
        self.ShieldProficiency = False
        #added a leading zero to these BAB and saves list so that the # in the list corresponds to the level.
        self.BAB = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]
        self.FortSave = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
        self.RefSave = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
        self.WillSave = [0,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12]
        self.StartingWealth=70

        #add more class stuff here