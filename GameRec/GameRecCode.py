import Games
import GameFunctions as func

print("Welcome to Sam's Game Recomendation System!")
print("First, how do you want to be recomended a new game?")
print("1: by your favorite catagory?  2: by your favorite games?")

choice1:int = -1
while(choice1 < 0 or choice1 > 2):
    try:
        choice1 = int(input())
    except:
        pass
    if (choice1 < 0 or choice1 > 2):
        print("please pick 1 or 2")

if (choice1==1):
    print("You chose by your favorite catagory!")
    print("Please enter the first letters of your favorite catagory")
    basicCata:list = func.simpList(Games.listOfCatagories,input())
    pickCata:str = ""
    while (pickCata == ""):
        if (len(basicCata)==0):
            print("Sadly we don't have that catagory")
            print("Try another letter!")
            basicCata:list = func.simpList(Games.listOfCatagories,input())
        elif (len(basicCata)==1):
            pickCata:str = basicCata[0]
            print("The catagory you picked is " + pickCata)
        else:
            print("Pick a catagory from this smaller list!")
            print(basicCata)
            basicCata:list = func.simpList(basicCata,input())


else:
    print("You chose by your favorite games!")
    print("please enter the first letters of your favorite game")
