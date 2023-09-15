import os
import datetime

#Constants
mealCycleDays = 21

#Date
firstDate = datetime.datetime(2023, 9, 25)
todayDate = datetime.datetime.today()
endTerm = datetime.datetime(2023, 10, 13)

#File
localDirection = os.path.dirname(__file__)
relativeDirection = "mealList/meal1.txt"
mealListDirection = os.path.join(localDirection, relativeDirection)

#Variable
programOn = True
daysFromFirstDay = todayDate - firstDate
daysUntilLastDay = endTerm - todayDate

def menu():
    while programOn:
        print(f"""
Today's Date: {(todayDate.year):4}/{(todayDate.month):2}/{(todayDate.day):2}
┌────────────────────────────┐
│School Meal Detection System│
└────────────────────────────┘

1. Meal today
2. Disclaimer

        """)
        try:
            menuChoice = int(input("Please enter the number of your choice."))
            if menuChoice == 1:
                showMeal()
            elif menuChoice == 2:
                showDisclaimer()
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

def readMealList():
    weekMealList = []
    weekLunch = []
    weekSupper = []
    week = 1
    day = 1 #1-7
    lunchOrSupper = True #True to be lunch, False to be dinner
    try:
        scoreboardFile = open(mealListDirection, "r")
        for line in scoreboardFile:
            if line == "|\n":
                lunchOrSupper = False
            elif line == "||\n":
                day = 1
                week += 1
                weekMealList.append([weekLunch, weekSupper])
                weekLunch = []
                weekSupper = []
                lunchOrSupper = True
            else:
                if day <= 7 and lunchOrSupper:
                    dataList = line.split("|")
                    normal = dataList[0]
                    Vegetarian = dataList[1]
                    weekLunch.append([normal, Vegetarian])
                elif day <= 7 and not(lunchOrSupper):
                    dataList = line.split("|")
                    normal = dataList[0]
                    Vegetarian = dataList[1]
                    weekSupper.append([normal, Vegetarian])
        scoreboardFile.close()
    except FileNotFoundError:
        print("\nMeal menu file not found, loading failed.\n")
    return weekMealList #To use, follow the formula of: weekMealList[week][0 for lunch, 1 for supper][day][0 for normal meal, 1 for vegetarian meal]

def showMeal():
    if daysUntilLastDay.days < 0:
        print("Michaelmas Term has ended.")
    else:
        weekMealList = readMealList()
        week = (daysFromFirstDay.days // 7)  + 1
        day = daysFromFirstDay.days - (7 * week) #1-7
        print("\nMeal today:\n")
        print("Lunch: ")
        print(f"""
    Normal: {weekMealList[week][0][day][0]}
    Vegetarian: {weekMealList[week][0][day][1]}
        """)
        print("Supper: ")
        print(f"""
    Normal: {weekMealList[week][1][day][0]}
    Vegetarian: {weekMealList[week][1][day][1]}
        """)

def showDisclaimer():
    print("\nThe creator of this program (DYZ) is not responsible for the accuracy of the information displayed, nor for any negative emotions the user may have as a result of not eating the meal displayed.")

menu()