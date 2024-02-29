import array as arr
import Games

def simpList(listy:list,subset:str):
    """simplifys a list based on if the first leters match a string"""
    newList:list = []
    subLen:int = len(subset)
    for elt in listy:
        if subset.lower() in elt.lower()[:subLen]:
            newList.append(elt)
    return newList

def simpListGame(listy:list,subset:str):
    """simplifys a list based on if the first leters match a string"""
    newList:list = []
    subLen:int = len(subset)
    for elt in listy:
        if subset.lower() in elt.name.lower()[:subLen]:
            newList.append(elt)
    return newList

def findCata(listy,genre:str):
    """returns a new list of all games of a genre"""
    foundList = []
    for cata in listy:
        if (cata[0].genre == genre):
            foundList = cata
    return foundList

def simpListList(listy:list,subset:str):
    """simplifes a list of lists of games"""
    newList = []
    subLen:int = len(subset)
    for sublist in listy:
        for game in sublist:
            if subset.lower() in game.name.lower()[:subLen]:
                newList.append(game)
    return newList
