# Imports

from flask import Flask as FlaskApplication
from flask import request as requestVariable
from flask import render_template as renderTemplate
from datetime import datetime

# Constants

# Variables

# Objects

myApp = FlaskApplication(__name__)

# Functions

@myApp.route("/")
def appIndex():
    return renderTemplate("00000.html")

@myApp.route("/helloWorld")
def helloWorldPage():
    return "Hello, World!"

#@myApp.route("/welcome")
#def welcomePageDefault():
#    return "Welcome to this website, PLACEHOLDER."
#
#@myApp.route("/welcome/<name>")
#def welcomePage(name):
#    return f"Welcome to this website, {name}."

@myApp.route("/welcome")
@myApp.route("/welcome/<name>")
def welcomePage(name: str = ""):
    return renderTemplate("00001.html", name = name)

@myApp.route("/你说得对")
def niShuoDeDui():
    return renderTemplate("00002.html")

@myApp.route("/functions")
def functionIndex():
    return "これはeine网站！"

@myApp.route("/functions/addition")
def additionFunction():
    firstNum = requestVariable.args.get("first", "")
    secondNum = requestVariable.args.get("second", "")
    if firstNum and secondNum:
        try:
            result = int(firstNum) + int(secondNum)
        except ValueError:
            return "Invalid Arguments"
        return f"{firstNum} + {secondNum} = {result}<br><br><br><br><br>Additional Info:<br><br><br>request.headers: {requestVariable.headers}<br><br>request.args: {requestVariable.args}<br><br>request.path: {requestVariable.path}<br><br>request.url: {requestVariable.url}"
    else:
        return "One or more arguments missing"

@myApp.route("/functions/birthday")
def birthdayFunction():
    today = datetime.today()
    try:
        birthdayMonth = int(requestVariable.args.get("month", ""))
        if (birthdayMonth >= 1) and (birthdayMonth <= 12):
            invalidMonth = False
        else:
            return "Number given out of range, please try again."
    except ValueError:
            return renderTemplate("00003.html", day = str(birthdayDay), month = str(birthdayMonth), daysUntil = False) 
    if birthdayMonth == 2:
        maxDate = 28
    elif (birthdayMonth == 4) or (birthdayMonth == 6) or (birthdayMonth == 9) or (birthdayMonth == 11):
        maxDate = 30
    else:
        maxDate = 31
    try:
        birthdayDay = int(requestVariable.args.get("day", ""))
        if not((birthdayMonth >= 1) and (birthdayMonth <= maxDate)):
            return renderTemplate("00003.html", day = str(birthdayDay), month = str(birthdayMonth), daysUntil = False) 
    except ValueError:
        return renderTemplate("00003.html", day = str(birthdayDay), month = str(birthdayMonth), daysUntil = False) 
    birthdayDate = datetime(today.year, birthdayMonth, birthdayDay)
    daysUntil = birthdayDate - today
    if daysUntil.days < 0:
        birthdayDate = datetime((today.year + 1), birthdayMonth, birthdayDay)
        daysUntil = birthdayDate - today
    daysUntilString = str(daysUntil.days + 1)
    #return f"There is {daysUntilString} days until your birthday."
    return renderTemplate("00003.html", day = str(birthdayDay), month = str(birthdayMonth), daysUntil = daysUntilString) 

@myApp.route("/functions/christmas")
def christmasFunction():
    today = datetime.today()
    christmasDate = datetime(today.year, 12, 25)
    daysUntil = christmasDate - today
    if daysUntil.days < 0:
        christmasDate = datetime((today.year + 1), 12, 25)
        daysUntil = christmasDate - today
    return f"There is {daysUntil.days + 1} days until the next Christmas."

# Main

if __name__ == '__main__':
    myApp.run(host="0.0.0.0", port=80, debug=True)