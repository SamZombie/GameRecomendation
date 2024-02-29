import Games
import GameFunctions as func
import random as rand

print("Welcome to Sam's Game Recomendation System!")

repeat = True
while(repeat):
    print("First, how do you want to be recomended a new game?")
    print("1: by your favorite category?  2: by your favorite game?")

    choice1:int = -1
    while(choice1 < 0 or choice1 > 2):
        try:
            choice1 = int(input())
        except:
            pass
        if (choice1 < 0 or choice1 > 2):
            print("please pick 1 or 2")

    if (choice1==1):
        print("You chose by your favorite category!")
        print("Please enter the first letters of your favorite category")
        basicCata:list = func.simpList(Games.listOfCategories,input())
        pickCata:str = ""
        while (pickCata == ""):
            if (len(basicCata)==0):
                print("Sadly we don't have that category")
                print("Try another letter!")
                basicCata:list = func.simpList(Games.listOfCategories,input())
            elif (len(basicCata)==1):
                pickCata:str = basicCata[0]
                print("The category you picked is " + pickCata)
            else:
                print("Pick a category from this smaller list!")
                print(basicCata)
                basicCata:list = func.simpList(basicCata,input())
        foundCata = func.findCata(Games.allGames,pickCata)
        print("What in this category do you want recomended?")
        print("1: a new game  2: an old game  3: any game")

        choice2:int = -1
        while(choice2 < 0 or choice2 > 3):
            try:
                choice2 = int(input())
            except:
                pass
            if (choice2 < 0 or choice2 > 3):
                print("please pick 1, 2, or 3")
        foundNewGame:Games.Game
        if (choice2==1):
            foundCata = sorted(foundCata,reverse=True,key=lambda x: x.year)
            foundNewGame = foundCata[0]
            print("The new game we picked for you is " + foundNewGame.name + " here is a bit of information about it.")
            print(foundNewGame)
        elif(choice2==2):
            foundCata = sorted(foundCata,key=lambda x: x.year)
            foundNewGame = foundCata[0]
            print("The old game we picked for you is " + foundNewGame.name + " here is a bit of information about it.")
            print(foundNewGame)
        else:
            randGameID:int = rand.randrange(0,len(foundCata))
            foundNewGame =foundCata[randGameID]
            print("The random game we picked for you in this catagory is " + foundNewGame.name + " here is a bit of information about it.")
            print(foundNewGame)

    else:
        print("You chose by your favorite games!")
        print("please enter the first letters of your favorite game")
        basicGame:list = func.simpListList(Games.allGames,input())
        pickGameName:str = ""
        pickGame:Games.Game
        while (pickGameName == ""):
            if (len(basicGame)==0):
                print("Sadly we don't have that game")
                print("Try another letter!")
                basicGame:list = func.simpListList(Games.allGames,input())
            elif (len(basicGame)==1):
                pickGame = basicGame[0]
                pickGameName = pickGame.name
                print("The game you picked is " + pickGameName)
            else:
                print("Pick a game from this smaller list!")
                gameNames = []
                for game in basicGame:
                    gameNames.append(game.name)
                print(gameNames)
                basicGame:list = func.simpListGame(basicGame,input())
        foundGame = func.findCata(Games.allGames,pickGame)

        print("What game like " + pickGameName + " do you want recomended?")
        print("1: a new game  2: an old game  3: any game")

        choice3:int = -1
        while(choice3 < 0 or choice3 > 3):
            try:
                choice3 = int(input())
            except:
                pass
            if (choice3 < 0 or choice3 > 3):
                print("please pick 1, 2, or 3")
        
        foundCata = func.findCata(Games.allGames,pickGame.genre)
        foundNewGame:Games.Game
        if (choice3==1):
            foundCata = sorted(foundCata,reverse=True,key=lambda x: x.year)
            foundNewGame = foundCata[0]
            print("The new game we picked for you is " + foundNewGame.name + " here is a bit of information about it.")
            print(foundNewGame)
        elif(choice3==2):
            foundCata = sorted(foundCata,key=lambda x: x.year)
            foundNewGame = foundCata[0]
            print("The old game we picked for you is " + foundNewGame.name + " here is a bit of information about it.")
            print(foundNewGame)
        else:
            randGameID:int = rand.randrange(0,len(foundCata))
            foundNewGame =foundCata[randGameID]
            print("The random game we picked for you in this catagory is " + foundNewGame.name + " here is a bit of information about it.")
            print(foundNewGame)

    print("Enter 'EXIT' to exit, or anything else to get another recomendation")
    if(input().lower() == "exit"):
        repeat = False
