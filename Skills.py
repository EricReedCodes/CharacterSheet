def loadSkillMatrix():
    Matrix = [[0 for x in range(7)] for x in range(36)]

    Matrix[0][0] = 'Skill'
    Matrix[0][1] = 'Total'
    Matrix[0][2] = 'Stat'
    Matrix[0][3] = 'Stat Mod'
    Matrix[0][4] = 'Class/XC'
    Matrix[0][5] = 'Ranks'
    Matrix[0][6] = 'Misc Mod'


    Matrix[1][0] = 'Acrobatics'
    Matrix[2][0] = 'Appraise'
    Matrix[3][0] = 'Bluff'
    Matrix[4][0] = 'Climb'
    Matrix[5][0] = 'Craft'
    Matrix[6][0] = 'Diplomacy'
    Matrix[7][0] = 'Disable Device'
    Matrix[8][0] = 'Disguise'
    Matrix[9][0] = 'Escape Artist'
    Matrix[10][0] = 'Fly'
    Matrix[11][0] = 'Handle Animal'
    Matrix[12][0] = 'Heal'
    Matrix[13][0] = 'Intimidate'
    Matrix[14][0] = 'Know_Arcana'
    Matrix[15][0] = 'Know_dungeoneering'
    Matrix[16][0] = 'Know_engineering'
    Matrix[17][0] = 'Know_geography'
    Matrix[18][0] = 'Know_history'
    Matrix[19][0] = 'Know_local'
    Matrix[20][0] = 'Know_nature'
    Matrix[21][0] = 'Know_nobility'
    Matrix[22][0] = 'Know_planes'
    Matrix[23][0] = 'Know_religion'
    Matrix[24][0] = 'Linguistics'
    Matrix[25][0] = 'Perception'
    Matrix[26][0] = 'Perform'
    Matrix[27][0] = 'Profession'
    Matrix[28][0] = 'Ride'
    Matrix[29][0] = 'Sense Motive'
    Matrix[30][0] = 'Sleight of Hand'
    Matrix[31][0] = 'Spellcraft'
    Matrix[32][0] = 'Stealth'
    Matrix[33][0] = 'Survival'
    Matrix[34][0] = 'Swim'
    Matrix[35][0] = 'Use Magic Device'

    Matrix[1][2] = 'Dex'
    Matrix[2][2] = 'Int'
    Matrix[3][2] = 'Cha'
    Matrix[4][2] = 'Str'
    Matrix[5][2] = 'Int'
    Matrix[6][2] = 'Cha'
    Matrix[7][2] = 'Dex'
    Matrix[8][2] = 'Cha'
    Matrix[9][2] = 'Dex'
    Matrix[10][2] = 'Dex'
    Matrix[11][2] = 'Cha'
    Matrix[12][2] = 'Wis'
    Matrix[13][2] = 'Cha'
    Matrix[14][2] = 'Int'
    Matrix[15][2] = 'Int'
    Matrix[16][2] = 'Int'
    Matrix[17][2] = 'Int'
    Matrix[18][2] = 'Int'
    Matrix[19][2] = 'Int'
    Matrix[20][2] = 'Int'
    Matrix[21][2] = 'Int'
    Matrix[22][2] = 'Int'
    Matrix[23][2] = 'Int'
    Matrix[24][2] = 'Int'
    Matrix[25][2] = 'Wis'
    Matrix[26][2] = 'Cha'
    Matrix[27][2] = 'Wis'
    Matrix[28][2] = 'Dex'
    Matrix[29][2] = 'Wis'
    Matrix[30][2] = 'Dex'
    Matrix[31][2] = 'Int'
    Matrix[32][2] = 'Dex'
    Matrix[33][2] = 'Wis'
    Matrix[34][2] = 'Str'
    Matrix[35][2] = 'Cha'
    return Matrix

def allocateSkillPoints(Matrix,SkillPoints):
    for x in range(0,36):
        print(Matrix[x])
    print("It's now time to allocate skill points.  First choose a skill and then choose how many points to allocate")
    print("You have",SkillPoints,"skill points to allocate.")
    while SkillPoints > 0:
        ValidSkillChoice = False
        while ValidSkillChoice == False:
            Skill = input("Enter the name of the skill without apostrophes.")
            #Skill = Skill.capitalize() - This lower cases subsequent words in skills with multiple words which caused failure.
            if [(index, row.index(Skill)) for index, row in enumerate(Matrix) if Skill in row] != []: #I don't understand exactly what this line means and am certain it could be more efficient
                ValidSkillChoice = True
            else:
                print("Sorry, that's not a valid option.")
        Ranks = int(input("Enter the number of skill points you wish to allocate to that skill."))
        if Ranks > SkillPoints:
            print("Sorry, you don't have that many skill points remaining.")
        else:
            for y in range(0,36):
                if Matrix[y][0]==Skill:
                    Matrix[y][5] = Matrix[y][5]+Ranks
            SkillPoints = SkillPoints - Ranks
    return Matrix

def setClassSkills(Matrix,ClassSkills):
    for x in range(1,36):
        if ClassSkills[x-1] == 'Class':
            Matrix[x][4] = 'Class'
    for y in range(1,36):
        if Matrix[y][4] == 0:
            Matrix[y][4] = 'XC'
    return Matrix

def CalculateSkillTotals(Matrix):
    for x in range(1,36):
        if Matrix[x][4] == 'Class' and Matrix[x][5]>=1:
            Matrix[x][1] = Matrix[x][3]+Matrix[x][5]+Matrix[x][6]+3
        else:
            Matrix[x][1] = Matrix[x][3]+Matrix[x][5]+Matrix[x][6]
    return Matrix

def addStatMods(Matrix,StrMod,DexMod,ConMod,IntMod,WisMod,ChaMod):
    for x in range(0,36):
        if Matrix[x][2] == 'Str':
            Matrix[x][3] = StrMod
        elif Matrix[x][2] == 'Dex':
            Matrix[x][3] = DexMod
        elif Matrix[x][2] == 'Con':
            Matrix[x][3] = ConMod
        elif Matrix[x][2] == 'Int':
            Matrix[x][3] = IntMod
        elif Matrix[x][2] == 'Wis':
            Matrix[x][3] = WisMod
        elif Matrix[x][2] == 'Cha':
            Matrix[x][3] = ChaMod
    return Matrix

def displaySkills(Matrix):
    for x in range(0,36):
        print(Matrix[x])
