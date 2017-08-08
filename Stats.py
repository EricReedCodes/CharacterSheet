import random
import math

#do I really want to have stats track all the different mods and initial rolls or should each stat just be a single number?
#in Excel it's been really nice to see how each stat (and every other numerical attribute a character has) adds up, but it seems like a pain in the ass here.
class Stat(object):
    def __init__(self, statRoll, racialMod, statTotal, statMod):
        self.self = self
        self.statRoll = statRoll
        self.racialMod = racialMod
        self.statTotal = statTotal
        self.statMod = statMod
    def set_racial_mod(self, RacialMod):
        self.racialMod = RacialMod
    def calculate_stat(self):
        self.statTotal = self.statRoll + self.racialMod
        self.statMod = math.floor((self.statTotal - 10) / 2)
    def get_stat_total(self):
        return self.statTotal
    def get_stat_mod(self):
        return self.statMod

def roll_stats(name):
#rolls a set of 7 stats, dropping the lowest.  Each stat is rolled as 4d6 dropping the lowest but adding ones.
#the highest six are assigned by the user, and then returned in the form of a list.
    Reroll = "Y"
    while Reroll in ("Y","y","yes"):
        statrolls = [0,0,0,0,0,0,0]
        for x in range(0,7):
            a = random.randint(1,6)
            b = random.randint(1,6)
            c = random.randint(1,6)
            d = random.randint(1,6)
            total = a+b+c+d - min(a,b,c,d)
            if min(a,b,c,d)==1:
                total+=1
            statrolls[x] = total
        statrolls.sort()
        statrolls.reverse()
        statrolls.pop(6)
        print("Right, here are yer stats,", name)
        print(statrolls)
        Reroll = input("Are these good enough for ya or does your privilege entitle you to roll again? (Enter 'Y' to reroll or 'N' to keep these stats.")
        #note that the user doesn't have to enter "N" as anything other than Y, y, or Yes will keep the stats.
        if Reroll in ("Y","y","yes"):
            print("Yep, I smelled your air of incestuous noble privilege a mile away.")
    #At some point control should be added so that the user can only enter the scores that were rolled.
    StrRoll = int(input("Please choose a score for Strength."))
    DexRoll = int(input("Please choose a score for Dexterity."))
    ConRoll = int(input("Please choose a score for Constitution."))
    IntRoll = int(input("Please choose a score for Intelligence."))
    WisRoll = int(input("Please choose a score for Wisdom."))
    ChaRoll = int(input("Please choose a score for Charisma."))
    stats = [StrRoll, DexRoll, ConRoll, IntRoll, WisRoll, ChaRoll]
    return (stats)

def display_stats(Str, StrMod, Dex, DexMod, Con, ConMod, Int, IntMod, Wis, WisMod, Cha, ChaMod):
    if Str>=10:
        print("Str: ", Str, "  +",StrMod)
    else:
        print("Str: ", Str, "  ",StrMod)
    if Dex>=10:
        print("Dex: ", Dex,"  +",DexMod)
    else:
        print("Dex: ", Dex, "  ",DexMod)
    if Con>=10:
        print("Con: ", Con,"  +",ConMod)
    else:
        print("Con: ", Con, "  ",ConMod)
    if Int>=10:
        print("Int: ", Int,"  +",IntMod)
    else:
            print("Int: ", Int, "  ",IntMod)
    if Wis>=10:
        print("Wis: ", Wis,"  +",WisMod)
    else:
            print("Wis: ", Wis, "  ",WisMod)
    if Cha>=10:
        print("Cha: ", Cha,"  +",ChaMod)
    else:
        print("Cha: ", Cha, "  ",ChaMod)

def add_stat_bonus(Stat): #will need something like this for fourth level bonuses but not sure how best to implement it.
    Stat+=1
