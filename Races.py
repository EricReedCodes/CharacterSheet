class Race(object):
    def __init__(self):
        pass
     #(self, strRacial, dexRacial, conRacial, wisRacial, intRacial, chaRacial, size, type, subtype, baseSpeed, bonusFeat, lowLightVision, darkVision):
     #   self.strRacial = strRacial
     #   self.dexRacial = dexRacial
     #   self.conRacial = conRacial
     #   self.wisRacial = wisRacial
     #   self.intRacial = intRacial
     #   self.chaRacial = chaRacial
     #   self.size = size
     #   self.type = type
     #   self.subtype = subtype
     #   self.baseSpeed = baseSpeed
     #   self.bonusFeat = bonusFeat
     #   self.lowLightVision = lowLightVision
     #   self.darkVision = darkVision
    def getStrRacial(self):
        return self.strRacial
    def getDexRacial(self):
        return self.dexRacial
    def getConRacial(self):
        return self.conRacial
    def getWisRacial(self):
        return self.wisRacial
    def getIntRacial(self):
        return self.intRacial
    def getChaRacial(self):
        return self.chaRacial
    def getRaceName(self):
        return self.raceName
    def getSize(self):
        return self.size
    def getType(self):
        return self.type
    def getSubtype(self):
        return self.subtype
    def getBaseSpeed(self):
        return self.baseSpeed
    def getBonusFeat(self):
        return self.bonusFeat
    def getLowLightVision(self):
        return self.lowLightVision
    def getDarkVision(self):
        return self.darkVision
#class dwarf(Race):
 #   def __init__(self, strRacial, dexRacial, conRacial, wisRacial, intRacial, chaRacial, size, type, subtype, baseSpeed, bonusFeat, lowLightVision, darkVision):
    def setRaceToDwarf(self):
        self.raceName = "Dwarf"
        self.strRacial = 0
        self.dexRacial = 0
        self.conRacial = 2
        self.intRacial = 0
        self.wisRacial = 2
        self.chaRacial = -2
        self.size = "M"
        self.type = "Humanoid"
        self.subtype = "Dwarf"
        self.baseSpeed = 20
        self.bonusFeat = 0
        self.lowLightVision = 0
        self.darkVision = 60
    def setRaceToHalfling(self):
        self.raceName = "Halfling"
        self.strRacial = -2
        self.dexRacial = 2
        self.conRacial = 0
        self.intRacial = 0
        self.wisRacial = 0
        self.chaRacial = 2
        self.size = "S"
        self.type = "Humanoid"
        self.subtype = "Halfling"
        self.baseSpeed = 20
        self.bonusFeat = 0
        self.lowLightVision = 0
        self.darkVision = 60
    def setRaceToHuman(self):
        self.raceName = "Human"
        self.strRacial = 0
        self.dexRacial = 0
        self.conRacial = 0
        self.intRacial = 0
        self.wisRacial = 0
        self.chaRacial = 0
        self.size = "M"
        self.type = "Humanoid"
        self.subtype = "Human"
        self.baseSpeed = 30
        self.bonusFeat = 1
        self.lowLightVision = 0
        self.darkVision = 0
        self.chooseBonus()
    def setRaceToHalfOrc(self):
        self.raceName="Half-Orc"
        self.strRacial = 0
        self.dexRacial = 0
        self.conRacial = 0
        self.intRacial = 0
        self.wisRacial = 0
        self.chaRacial = 0
        self.size = "M"
        self.type = "Humanoid"
        self.subtype = "Half-Orc?"
        self.baseSpeed = 30
        self.bonusFeat = 0
        self.lowLightVision = 0
        self.darkVision = 60
        self.chooseBonus()

    def chooseBonus(self): #This is for races like humans, half-orcs, and half-elves to choose a stat for their +2 bonus.
        statbonus = 99
        while statbonus >6:
            try:
                statbonus = int(input("Please choose a stat for your +2 bonus: (1) Str, (2) Dex, (3) Con, (4) Int, (5) Wis, or (6) Cha."))
                if statbonus==1:
                    self.strRacial=2
                elif statbonus==2:
                    self.dexRacial=2
                elif statbonus==3:
                    self.conRacial=2
                elif statbonus==4:
                    self.intRacial=2
                elif statbonus==5:
                    self.wisRacial=2
                elif statbonus==6:
                    self.chaRacial=2
                else:
                    print("Please enter a number from 1-6.")
            except ValueError:
                print("Please enter a number from 1-6.")

def chooseRace():
    r = Race()
    racechoice = 99 #99 is an arbitrary number that is an invalid option below in order to begin the while loop.
    while racechoice >7:
        try:
            racechoice = int(input("Please choose a race:  (1) Dwarf, (2) Elf, (3) Gnome, (4) Half-Elf, (5) Half-Orc, (6) Halfling, (7) Human"))
            if racechoice==1:
                r.setRaceToDwarf()
            elif racechoice==2: #Elf
                print("coming soon")
                racechoice=99
            elif racechoice==3: #Gnome
                print("coming soon")
                racechoice=99
            elif racechoice==4: #Half-Elf
                print("coming soon")
                racechoice=99
            elif racechoice==5: #Half-Orc
                r.setRaceToHalfOrc()
            elif racechoice==6:
                r.setRaceToHalfling()
            elif racechoice==7:
                r.setRaceToHuman()
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Please choose a valid numerical option.")
            racechoice = 99
    return r
