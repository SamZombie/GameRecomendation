import array as arr

listOfCategories = [ "Fighting", "Racing", "Stealth", "Adventure", "Horror", "Shooter", "Survival", "Platformer", "Strategy", "Simulation"]

class Game:
    def __init__(self,name:str,genre:str,year:int):
        self.name = name
        self.genre = genre
        self.year = year
    def __str__(self) -> str:
        ret = self.name + " was published in " + str(self.year) + " and is mainly a " + self.genre.lower() + " game."
        return ret
    
#init fighting games
streetFighter = Game("Street Fighter", "Fighting", 1987)
superSB = Game("Super Smash Bros.", "Fighting", 1999)
tekken = Game("Tekken", "Fighting", 1994)
mortalKombat = Game("Mortal Kombat", "Fighting", 1992)
soulcalibur = Game("Soulcalibur","Fighting", 1998)
fighting = [streetFighter,superSB,tekken,mortalKombat,soulcalibur]

#init racing games
granTurismo = Game("Gran Turismo","Racing",1997)
marioKart = Game("Mario Kart","Racing",1992)
needForSpeed = Game("Need for Speed","Racing",1994)
forzaHorizon = Game("Forza Horizon","Racing",2012)
burnOut = Game("Burnout","Racing",2001)
racing = [granTurismo,marioKart,needForSpeed,forzaHorizon,burnOut]

#init stealth games
hitman = Game("Hitman","Stealth",2000)
dishonored = Game("Dishonored","Stealth",2012)
assassinCreed = Game("Assassin's Creed","Stealth",2007)
deusEx = Game("Deus Ex","Stealth",2000)
watchDogs = Game("Watch Dogs","Stealth",2014)
stealth = [hitman,dishonored,assassinCreed,deusEx,watchDogs]

#init adventure
fallout = Game("Fallout","Adventure",1997)
bioShock = Game("BioShock","Adventure",2007)
outerWild = Game("Outer Wild","Adventure",2019)
redDeadRedemption = Game("Red Dead Redemption","Adventure",2010)
theWitcher = Game("The Witcher","Adventure",2007)
adventure = [fallout,bioShock,outerWild,redDeadRedemption,theWitcher]

#init horror games
deadSpace = Game("Dead Space","Horror",2008)
residentEvil = Game("Resident Evil","Horror",1996)
silentHill = Game("Silent Hill","Horror",1999)
fiveNights = Game("Five Nights at Freddy's","Horror",2014)
untilDawn = Game("Untill Dawn","Horror",2015)
horror = [deadSpace,residentEvil,silentHill,fiveNights,untilDawn]

#init shooter games
farCry = Game("Far Cry","Shooter",2004)
titanFall = Game("Titanfall","Shooter",2014)
callOfDuty = Game("Call of Duty","Shooter",2003)
halo = Game("Halo","Shooter",2001)
battlefield = Game("Battlefield","Shooter",2002)
shooter = [farCry,titanFall,callOfDuty,halo,battlefield]

#init survival games
minecraft = Game("Minecraft","Survival",2009)
subnautica = Game("Subnautica","Survival",2014)
terraria = Game("Terraria","Survival",2011)
arc = Game("ARC: Survival Evolved","Survival",2015)
rust = Game("Rust","Survival",2013)
survival = [minecraft,subnautica,terraria,arc,rust]

#init platformer games
superMario = Game("Super Mario","Platformer",1985)
sonic = Game("Sonic","Platformer",1991)
celeste = Game("Celeste","Platformer",2018)
hollowKnight = Game("Hollow Knight","Platformer",2017)
shovelKnight = Game("Shovel Knight","Platformer",2014)
platformer = [superMario,sonic,celeste,hollowKnight,shovelKnight]

#init strategy games
civilization = Game("Civilization","Strategy",1991)
crusaderKings = Game("Crusader Kings","Strategy",2004)
anno = Game("Anno","Strategy",1998)
totalWar = Game("Total War","Strategy",2000)
starCraft = Game("StarCraft","Strategy",1998)
strategy = [civilization,crusaderKings,anno,totalWar,starCraft]

#init simulation games
theSims = Game("The SIMS","Simulation",2000)
pcBuildingSim = Game("PC Building Simulator","Simulation",2018)
flightSim = Game("Microsoft Flight Simulator","Simulation",1982)
farmingSim = Game("Farming Simulator","Simulation",2008)
stardewValley = Game("Stardew Valley","Simulation",2016)
simulation = [theSims,pcBuildingSim,flightSim,farmingSim,stardewValley]

allGames = [fighting , racing , stealth , adventure , horror , shooter , survival , platformer , strategy , simulation]
