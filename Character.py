import Stats

class Character(object):
    def init(self, name, character_level, numfeats, hitpoints):
        self.name = name
        self.numfeats = numfeats
        self.character_level = character_level
        self.hitpoints = hitpoints
    def create_name(self):
        print("Ye dare to enter this realm as new character, eh?")
        name = input("Do ye have a name or shall we just call you stupid?")
        if name in("Yes","yes","y"):
            print("Ok, stupid it is then.")
            name = "stupid"
        self.name = name
    def get_name(self):
        return self.name
    def get_numfeats(self):
        return self.numfeats
    def add_feat(self):
        self.numfeats+=1
    def get_hitpoints(self):
        return self.hitpoints
    def add_hitpoints(self, added_hp):
        self.hitpoints+=added_hp
    def level_up(self):
        self.character_level+=1
        if self.character_level.__mod__(2)==1:
            self.numfeats+=1
        #to make this work I either need to pass around all six stats to the level_up function, move stats to Character, or think of something else.
        # if self.character_level.__mod__(4)==0:
        #     Stats.add_stat_bonus(Stat)
