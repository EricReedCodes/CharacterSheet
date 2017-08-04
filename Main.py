import Stats
import Races
from SavingThrows import SavingThrows
import math
import Skills
import Class

statrolls = Stats.rollStats()
Str = Stats.Stat(statrolls[0],0,statrolls[0],math.floor((statrolls[0] -10) /2))
Dex = Stats.Stat(statrolls[1],0,statrolls[1],math.floor((statrolls[1] -10) /2))
Con = Stats.Stat(statrolls[2],0,statrolls[2],math.floor((statrolls[2] -10) /2))
Int = Stats.Stat(statrolls[3],0,statrolls[3],math.floor((statrolls[3] -10) /2))
Wis = Stats.Stat(statrolls[4],0,statrolls[4],math.floor((statrolls[4] -10) /2))
Cha = Stats.Stat(statrolls[5],0,statrolls[5],math.floor((statrolls[5] -10) /2))

r = Races.chooseRace()
Class = Class.chooseClass()
Class.setLevel(1)

#Having these 13 lines of code here just to update stats to reflect racial mods seems quite tedious, consider making methods to update all stats at once.
Str.setRacialMod(r.getStrRacial())
Dex.setRacialMod(r.getDexRacial())
Con.setRacialMod(r.getConRacial())
Int.setRacialMod(r.getIntRacial())
Wis.setRacialMod(r.getWisRacial())
Cha.setRacialMod(r.getChaRacial())
Str.calculateStat()
Dex.calculateStat()
Con.calculateStat()
Int.calculateStat()
Wis.calculateStat()
Cha.calculateStat()
Stats.displayStats(Str.getStatTotal(),Str.getStatMod(),Dex.getStatTotal(),Dex.getStatMod(),Con.getStatTotal(),Con.getStatMod(),Int.getStatTotal(),Int.getStatMod(),Wis.getStatTotal(),Wis.getStatMod(),Cha.getStatTotal(),Cha.getStatMod())

st = SavingThrows()
st.CalculateSaves(Class.getFortSave(),Class.getRefSave(),Class.getWillSave(),Con.getStatMod(),Dex.getStatMod(),Wis.getStatMod())
st.displaySaves()

Matrix = Skills.loadSkillMatrix()
Matrix = Skills.addStatMods(Matrix,Str.getStatMod(),Dex.getStatMod(),Con.getStatMod(),Int.getStatMod(),Wis.getStatMod(),Cha.getStatMod())
Matrix = Skills.setClassSkills(Matrix,Class.getClassSkills())
Matrix = Skills.allocateSkillPoints(Matrix,Class.getSkillPoints(Int.getStatMod()))
Matrix = Skills.CalculateSkillTotals(Matrix)
Skills.displaySkills(Matrix)
