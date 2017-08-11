import Stats
import SavingThrows

class Character(object):
    def init(self, name, character_level, numfeats, hitpoints, savingthrows, str, dex, con, int, wis, cha):
        self.name = name
        self.numfeats = numfeats
        self.character_level = character_level
        self.hitpoints = hitpoints
        self.savingthrows = savingthrows
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

    #name block
    def create_name(self):
        print("Ye dare to enter this realm as new character, eh?")
        name = input("Do ye have a name or shall we just call you stupid?")
        if name in("Yes","yes","y"):
            print("Ok, stupid it is then.")
            name = "stupid"
        self.name = name
    def get_name(self):
        return self.name

    #stat block
    def get_str(self):
        return self.str
    def get_dex(self):
        return self.dex
    def get_con(self):
        return self.con
    def get_int(self):
        return self.int
    def get_wis(self):
        return self.wis
    def get_cha(self):
        return self.cha
    def update_stats(self, str, dex, con, int, wis, cha):
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

    #feat block
    def get_numfeats(self):
        return self.numfeats
    def add_feat(self):
        self.numfeats+=1

    #hps
    def get_hitpoints(self):
        return self.hitpoints
    def add_hitpoints(self, added_hp):
        self.hitpoints+=added_hp

    #level up
    def level_up(self):
        self.character_level+=1
        if self.character_level.__mod__(2)==1:
            self.numfeats+=1
        if self.character_level.__mod__(4)==0:
            statbonus = 99
            while statbonus > 6:
                try:
                    statbonus = int(input("Please choose a stat for your +1 bonus: (1) Str, (2) Dex, (3) Con, (4) Int, (5) Wis, or (6) Cha."))
                    if statbonus == 1:
                        self.str.add_level_bonus()
                    elif statbonus == 2:
                        self.dex.add_level_bonus()
                    elif statbonus == 3:
                        self.con.add_level_bonus()
                    elif statbonus == 4:
                        self.int.add_level_bonus()
                    elif statbonus == 5:
                        self.wis.add_level_bonus()
                    elif statbonus == 6:
                        self.cha.add_level_bonus()
                    else:
                        print("Please enter a number from 1-6.")
                except ValueError:
                    print("Please enter a number from 1-6.")