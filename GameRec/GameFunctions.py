import Games

def simpList(listy:list,subset:str):
    newList:list = []
    subLen:int = len(subset)
    for elt in listy:
        if subset.lower() in elt.lower()[:subLen]:
            newList.append(elt)
    return newList