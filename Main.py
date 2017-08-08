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

char = Character.Character()
char.create_name()
char.init(char.get_name(),1,1,0)

statrolls = Stats.roll_stats(char.get_name())
Str = Stats.Stat(statrolls[0],0,statrolls[0],math.floor((statrolls[0] -10) /2))
Dex = Stats.Stat(statrolls[1],0,statrolls[1],math.floor((statrolls[1] -10) /2))
Con = Stats.Stat(statrolls[2],0,statrolls[2],math.floor((statrolls[2] -10) /2))
Int = Stats.Stat(statrolls[3],0,statrolls[3],math.floor((statrolls[3] -10) /2))
Wis = Stats.Stat(statrolls[4],0,statrolls[4],math.floor((statrolls[4] -10) /2))
Cha = Stats.Stat(statrolls[5],0,statrolls[5],math.floor((statrolls[5] -10) /2))

print("feats:",char.get_numfeats())
r = Races.choose_race(char)
print("feats",char.get_numfeats())
Class = Class.choose_class()
Class.set_level(1)
Class.level_one(char)
print("feats:",char.get_numfeats())

#Having these 13 lines of code here just to update stats to reflect racial mods seems quite tedious, consider making methods to update all stats at once.
Str.set_racial_mod(r.get_str_racial())
Dex.set_racial_mod(r.get_dex_racial())
Con.set_racial_mod(r.get_con_racial())
Int.set_racial_mod(r.get_int_racial())
Wis.set_racial_mod(r.get_wis_racial())
Cha.set_racial_mod(r.get_cha_racial())
Str.calculate_stat()
Dex.calculate_stat()
Con.calculate_stat()
Int.calculate_stat()
Wis.calculate_stat()
Cha.calculate_stat()
Stats.display_stats(Str.get_stat_total(),Str.get_stat_mod(),Dex.get_stat_total(),Dex.get_stat_mod(),Con.get_stat_total(),Con.get_stat_mod(),Int.get_stat_total(),Int.get_stat_mod(),Wis.get_stat_total(),Wis.get_stat_mod(),Cha.get_stat_total(),Cha.get_stat_mod())

st = SavingThrows()
st.calculate_saves(Class.get_fort_save(),Class.get_ref_save(),Class.get_will_save(),Con.get_stat_mod(),Dex.get_stat_mod(),Wis.get_stat_mod())
st.display_saves()

#disabling skill stuff since it's spammy, but so far it's working as intended
# Matrix = Skills.load_skill_matrix()
# Matrix = Skills.add_stat_mods(Matrix,Str.get_stat_mod(),Dex.get_stat_mod(),Con.get_stat_mod(),Int.get_stat_mod(),Wis.get_stat_mod(),Cha.get_stat_mod())
# Matrix = Skills.set_class_skills(Matrix,Class.get_class_skills())
# Matrix = Skills.allocate_skill_points(Matrix,Class.get_skill_points(Int.get_stat_mod())-Skills.get_skill_points_used(Matrix)) #obviously no skills have been used at this point, but I want to get in the habit of using this method in this way
# Matrix = Skills.calculate_skill_totals(Matrix)
#Skills.display_skills(Matrix)

char.add_hitpoints(Class.get_hit_die() + Con.get_stat_mod())
print("hps at level 1:", char.get_hitpoints())

#Eventually everything that happens upon leveling should go into a function.
Class.level_up(char,Con.get_stat_mod())
Class.level_two(char)
#char.add_hitpoints(random.randint(1,Class.get_hit_die())+Con.get_stat_mod())
print("HP at lvl 2:", char.get_hitpoints())
print("Feats at lvl 2:",char.get_numfeats())
st.calculate_saves(Class.get_fort_save(),Class.get_ref_save(),Class.get_will_save(),Con.get_stat_mod(),Dex.get_stat_mod(),Wis.get_stat_mod())
#Matrix = Skills.allocate_skill_points(Matrix,Class.get_skill_points(Int.get_stat_mod())-Skills.get_skill_points_used(Matrix))
#BAB automatically goes up
Class.level_up(char,Con.get_stat_mod())
Class.level_three(char)
print("HP at lvl 3:", char.get_hitpoints())
print("Feats at lvl 3:",char.get_numfeats())
