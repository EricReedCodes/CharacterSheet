import random

class ClassLevels (object):
    def __init__(self):
        pass
    def get_level(self):
        return self.Level
    def set_level(self,Level):
        self.Level= Level
    def level_up(self,character,con_mod):
        self.Level = self.Level+1
        character.add_hitpoints(random.randint(1,self.get_hit_die())+con_mod)
        character.level_up()
    def get_hit_die(self):
        return self.HitDie
    def get_skill_points(self,IntMod):
        return self.Level*(self.SkillPoints+IntMod)
    def has_simple_weapon_proficiency(self):
        return self.SimpleWeaponProficiency
    def has_martial_weapon_proficiency(self):
        return self.MartialWeaponProficiency
    def has_light_armor_proficiency(self):
        return self.LightArmorProficiency
    def has_medium_armor_proficiency(self):
        return self.MediumArmorProficiency
    def has_heavy_armor_proficiency(self):
        return self.HeavyArmorProficiency
    def has_shield_proficiency(self):
        return self.ShieldProficiency
    def get_bab(self):
        return self.BAB[self.get_level()]
    def get_fort_save(self):
        return self.FortSave[self.get_level()]
    def get_ref_save(self):
        return self.RefSave[self.get_level()]
    def get_will_save(self):
        return self.WillSave[self.get_level()]
    def get_class_skills(self):
        return self.ClassSkills

def choose_class():
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
