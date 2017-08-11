import random

from Class import ClassLevels

class Fighter(ClassLevels):
    def __init__(self):
        self.level = 0
        self.HitDie = 10
        self.SkillPoints = 2
        #these XC and Class skills align with the order of skills in the Skills class.
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
        self.RefSave = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
        self.WillSave = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
        self.StartingWealth = 175
        self.bravery = 0
        self.armor_training = 0
        self.weapon_training = 0
        self.armor_mastery = False
        self.weapon_mastery = False
    def level_up(self,character):
        self.level = self.level+1
        if self.level==1:
            character.add_hitpoints(self.get_hit_die() + character.get_con().get_stat_mod())
        else:
            character.add_hitpoints(random.randint(1,self.get_hit_die())+character.get_con().get_stat_mod())
        character.level_up()
        #Fighter-specific leveling stuff
        if self.level==1:
            character.add_feat()
        if self.level.__mod__(2) == 0:
            character.add_feat()
        if self.level.__mod__(4)==2:
            self.bravery +=1
        if self.level.__mod__(3)==4:
            self.armor_training+=1
        if self.level.__mod__(4)==5:
            self.weapon_training+=1
        if self.level == 19:
            self.armor_mastery = True
        if self.level == 20:
            self.weapon_mastery = True