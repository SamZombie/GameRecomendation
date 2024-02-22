listOfCatagories = [ "Fighting", "Racing", "Stealth", "Adventure", "Tabletop", "Shooter", "Survival","Platformer", "Strategy","Simulation"]

class Game:
    def __init__(self,name:str,genre:str,year:int):
        self.name = name
        self.genre = genre
        self.year = year
    def __str__(self) -> str:
        ret = self.name + " was published in " + str(self.year) + " and is mainly a  " + self.genre.lower() + " game."
        return ret
    
#init fighting games
streetFighter = Game("Street Fighter", "Fighting", 1987)
superSB = Game("Super Smash Bros.", "Fighting", 1999)
tekken = Game("Tekken", "Fighting", 1994)
mortalKombat = Game("Mortal Kombat", "Fighting", 1992)
soulcalibur = Game("Soulcalibur","Fighting", 1998)
"""
#init racing games
granTurismo = Game()
marioKart = Game()
needForSpeed = Game()
forzaHorizon = Game()
burnOut = Game()

#init stealth games
hitman = Game()
dishonored = Game()
assassinCreed = Game()
deusEx = Game()
watchDogs = Game()

#init adventure


#init tabletop games


#init shooter games


#init survival games


#init platformer games


#init strategy games


#init simulation games
"""