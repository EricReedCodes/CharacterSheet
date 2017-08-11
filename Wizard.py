import random

from Class import ClassLevels

class Wizard(ClassLevels):
    def __init__(self):
        self.level = 0
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
        self.arcane_bond = ""
        self.arcane_school = "universalist"
        self.opposition_school = ""
        self.opposition_school2 = ""
    def level_up(self,character):
        self.level = self.level+1
        if self.level==1:
            character.add_hitpoints(self.get_hit_die() + character.get_con().get_stat_mod())
        else:
            character.add_hitpoints(random.randint(1,self.get_hit_die())+character.get_con().get_stat_mod())
        character.level_up()
        #Wizard-specific leveling stuff
        if self.level ==1:
            bond = 3
            while bond not in (1,2):
                try:
                    bond = int(input("Would you like to have 1) a bonded object or 2) a familiar?"))
                    if bond ==1:
                        self.arcane_bond = input("What object would you like to bond?")
                    elif bond==2:
                        self.arcane_bond = input("What animal would you like for your familiar?")
                        #Once I connect this to a database, there should be a table of familiars with all the bonuses, and the user could choose a familiar from this list:  http://www.d20pfsrd.com/classes/core-classes/wizard/familiar
                    else:
                        print("Choose 1 or 2, jackass.")
                except ValueError:
                        print("Stop wasting my time and choose 1 or 2.")
            print("Would you like to specialize?  You can enter a number to specialize in any of the following schools.  Any other entry will result in a choise of universalist")
            spec = input("1) abjuration 2) conjuration 3) divination 4) enchantment 5) evocation 6) illusion 7) necromancy 8) sin magic 9) transmutation")
            if spec==1:
                self.arcane_school = "abjuration"
            if spec==2:
                self.arcane_school = "conjuration"
            if spec==3:
                self.arcane_school = "divination"
            if spec==4:
                self.arcane_school = "enchantment"
            if spec==5:
                self.arcane_school = "evocation"
            if spec==6:
                self.arcane_school = "illusion"
            if spec==7:
                self.arcane_school = "necromancy"
            if spec==8:
                self.arcane_school = "sin magic"
            if spec==9:
                self.arcane_school = "transmutation"
            #if wizard is not universalist he/she must choose two opposition schools
            if self.arcane_school != "universalist":
                print("You must now choose two opposition schools.")
                opp = 10
                while opp not in (1,2,3,4,5,6,7,8,9):
                    try:
                        opp = int(input("1) abjuration 2) conjuration 3) divination 4) enchantment 5) evocation 6) illusion 7) necromancy 8) sin magic 9) transmutation"))
                        if opp == 1:
                            self.opposition_school = "abjuration"
                        elif opp == 2:
                            self.opposition_school = "conjuration"
                        elif opp == 3:
                            self.opposition_school = "divination"
                        elif opp == 4:
                            self.opposition_school = "enchantment"
                        elif opp == 5:
                            self.opposition_school = "evocation"
                        elif opp == 6:
                            self.opposition_school = "illusion"
                        elif opp == 7:
                            self.opposition_school = "necromancy"
                        elif opp == 8:
                            self.opposition_school = "sin magic"
                        elif opp == 9:
                            self.opposition_school = "transmutation"
                        else:
                            print("Choose a valid entry, wise guy.")
                    except ValueError:
                            print("Choose a valid entry, wise guy.")
                print("Now choose a second opposition school.")
                opp = 10
                while opp not in (1,2,3,4,5,6,7,8,9):
                    try:
                        opp = int(input("1) abjuration 2) conjuration 3) divination 4) enchantment 5) evocation 6) illusion 7) necromancy 8) sin magic 9) transmutation"))
                        if opp == 1:
                            self.opposition_school2 = "abjuration"
                        elif opp == 2:
                            self.opposition_school2 = "conjuration"
                        elif opp == 3:
                            self.opposition_school2 = "divination"
                        elif opp == 4:
                            self.opposition_school2 = "enchantment"
                        elif opp == 5:
                            self.opposition_school2 = "evocation"
                        elif opp == 6:
                            self.opposition_school2 = "illusion"
                        elif opp == 7:
                            self.opposition_school2 = "necromancy"
                        elif opp == 8:
                            self.opposition_school2 = "sin magic"
                        elif opp == 9:
                            self.opposition_school2 = "transmutation"
                        else:
                            print("Choose a valid entry, wise guy.")
                    except ValueError:
                            print("Choose a valid entry, wise guy.")