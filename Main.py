import math

import Stats
import Races
from SavingThrows import SavingThrows
import Skills
import Class
import Character

#Python style that I have started trying to use after extensively not following this style
#ClassNames: CapWords
#TypeVariables: CapWords (what is a type variable?)
#package and module_names: lowercase_with_underscores_if_it_improves_readability
#function_names: lowercase_with_underscores_if_it_improves_readability
#method_names: lowercase_with_underscores_if_it_improves_readability
#instance variables: lowercase_with_underscores_if_it_improves_readability

st = SavingThrows()
str = Stats.Stat(0,0,0,0,0,0)
dex = Stats.Stat(0,0,0,0,0,0)
con = Stats.Stat(0,0,0,0,0,0)
int = Stats.Stat(0,0,0,0,0,0)
wis = Stats.Stat(0,0,0,0,0,0)
cha = Stats.Stat(0,0,0,0,0,0)

char = Character.Character()
char.create_name()
char.init(char.get_name(),0,0,0,st,str, dex, con, int, wis, cha)
#WARNING!!! Right now saving throws are getting passed into the character but not being updated nor used in any way.
#Either decide if it would make sense to put them under Character or remove this parameter.

statrolls = Stats.roll_stats(char.get_name())
str = Stats.Stat(statrolls[0],0,0,0,statrolls[0],math.floor((statrolls[0] -10) /2))
dex = Stats.Stat(statrolls[1],0,0,0,statrolls[1],math.floor((statrolls[1] -10) /2))
con = Stats.Stat(statrolls[2],0,0,0,statrolls[2],math.floor((statrolls[2] -10) /2))
int = Stats.Stat(statrolls[3],0,0,0,statrolls[3],math.floor((statrolls[3] -10) /2))
wis = Stats.Stat(statrolls[4],0,0,0,statrolls[4],math.floor((statrolls[4] -10) /2))
cha = Stats.Stat(statrolls[5],0,0,0,statrolls[5],math.floor((statrolls[5] -10) /2))
char.update_stats(str,dex,con,int,wis,cha)

print("feats:",char.get_numfeats())
r = Races.choose_race(char)
print("feats",char.get_numfeats())
Class = Class.choose_class()
Class.level_up(char) #this brings char to level 1
print("feats:",char.get_numfeats())

#Having these 13 lines of code here just to update stats to reflect racial mods seems quite tedious, consider making methods to update all stats at once.
str.set_racial_mod(r.get_str_racial())
dex.set_racial_mod(r.get_dex_racial())
con.set_racial_mod(r.get_con_racial())
int.set_racial_mod(r.get_int_racial())
wis.set_racial_mod(r.get_wis_racial())
cha.set_racial_mod(r.get_cha_racial())
char.update_stats(str,dex,con,int,wis,cha)
Stats.display_stats(str.get_stat_total(),str.get_stat_mod(),dex.get_stat_total(),dex.get_stat_mod(),con.get_stat_total(),con.get_stat_mod(),int.get_stat_total(),int.get_stat_mod(),wis.get_stat_total(),wis.get_stat_mod(),cha.get_stat_total(),cha.get_stat_mod())

st = SavingThrows()
st.calculate_saves(Class.get_fort_save(),Class.get_ref_save(),Class.get_will_save(),con.get_stat_mod(),dex.get_stat_mod(),wis.get_stat_mod())
st.display_saves()

#disabling skill stuff since it's spammy, but so far it's working as intended
# Matrix = Skills.load_skill_matrix()
# Matrix = Skills.add_stat_mods(Matrix,Str.get_stat_mod(),Dex.get_stat_mod(),Con.get_stat_mod(),Int.get_stat_mod(),Wis.get_stat_mod(),Cha.get_stat_mod())
# Matrix = Skills.set_class_skills(Matrix,Class.get_class_skills())
# Matrix = Skills.allocate_skill_points(Matrix,Class.get_skill_points(Int.get_stat_mod())-Skills.get_skill_points_used(Matrix)) #obviously no skills have been used at this point, but I want to get in the habit of using this method in this way
# Matrix = Skills.calculate_skill_totals(Matrix)
#Skills.display_skills(Matrix)

print("hps at level 1:", char.get_hitpoints())

#Eventually everything that happens upon leveling should go into a function.
Class.level_up(char)
print("HP at lvl 2:", char.get_hitpoints())
print("Feats at lvl 2:",char.get_numfeats())
st.calculate_saves(Class.get_fort_save(),Class.get_ref_save(),Class.get_will_save(),con.get_stat_mod(),dex.get_stat_mod(),wis.get_stat_mod())
#Matrix = Skills.allocate_skill_points(Matrix,Class.get_skill_points(Int.get_stat_mod())-Skills.get_skill_points_used(Matrix))
#BAB automatically goes up
Class.level_up(char)
print("HP at lvl 3:", char.get_hitpoints())
print("Feats at lvl 3:",char.get_numfeats())

Class.level_up(char)
Stats.display_stats(str.get_stat_total(),str.get_stat_mod(),dex.get_stat_total(),dex.get_stat_mod(),con.get_stat_total(),con.get_stat_mod(),int.get_stat_total(),int.get_stat_mod(),wis.get_stat_total(),wis.get_stat_mod(),cha.get_stat_total(),cha.get_stat_mod())
