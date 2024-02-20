# Imports

from flask import Flask as FlaskApplication
from flask import request as requestVariable
from flask import render_template as renderTemplate
from datetime import datetime
from os import path as filePath

# Constants

fileFolderDirection = filePath.join(filePath.dirname(__file__), "txtfile/flask")
chatroomHistoryDirection = filePath.join(fileFolderDirection, "chatroomHistory.txt")

# Variables

# Classes

class Message():

    def __init__(self, username: str, ip: str, content: str) -> None:
        if username == "":
            self._username = "Anonymous"
        else:
            self._username = str(username)
        self._ip = str(ip)
        self._content = str(content)
    
    def getUsername(self) -> str:
        return self._username
    
    def getIp(self) -> str:
        return self._ip
    
    def getContent(self) -> str:
        return self._content

    def getFormattedMessage(self) -> str:
        return f"{self._username} (IP: {self._ip})\n(Greenwich Time: {datetime.today()})\n\n   {self._content}\n\n\n"

# Objects

myApp = FlaskApplication(__name__)

# Functions

def chatroomMessageHistoryFile2List() -> list:
    chatroomMessageList = []
    messageLineCount = 0
    with open(chatroomHistoryDirection, "r") as chatroomHistoryFile:
        chatroomMessageRawList = chatroomHistoryFile.readlines()
    for line in chatroomMessageRawList:
        chatroomMessageList.append(line.replace("\n", " "))
        messageLineCount += 1
    return chatroomMessageList

def checkSpam(message: Message) -> bool:
    with open(chatroomHistoryDirection, "r") as chatroomHistoryFile:
        chatroomMessageRawList = chatroomHistoryFile.readlines()
    #print(f"\nfirst line:\n{message._username} (IP: {message._ip})\nchatroomMessageRawList[-10:]:\n{chatroomMessageRawList[-64:]}\n\nthird line:\n{message._content}\nchatroomMessageRawList[-3:]:\n{chatroomMessageRawList[-16:]}\n")
    if ((f"{message._username} (IP: {message._ip})" + "\n") in chatroomMessageRawList[-64:]) and ((f"   {message._content}" + "\n") in chatroomMessageRawList[-16:]):
        return True
    else:
        return False

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

@myApp.route("/welcome", methods = ["POST", "GET"])
def welcomePage():
    if requestVariable.method == "POST":
        typedName = requestVariable.form["visitorName"]
    else:
        typedName = ""
    return renderTemplate("00001.html", name = typedName)

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

@myApp.route("/functions/birthday", methods = ["POST", "GET"])
def birthdayFunction():
    if requestVariable.method == "POST":
        today = datetime.today()
        try:
            birthdayMonth = int(requestVariable.form["visitorBirthdayMonth"])
            if not((birthdayMonth >= 1) and (birthdayMonth <= 12)):
                return renderTemplate("00003.html", daysUntil = False)
        except ValueError:
                return renderTemplate("00003.html", daysUntil = False)
        if birthdayMonth == 2:
            maxDate = 28
        elif (birthdayMonth == 4) or (birthdayMonth == 6) or (birthdayMonth == 9) or (birthdayMonth == 11):
            maxDate = 30
        else:
            maxDate = 31
        try:
            birthdayDay = int(requestVariable.form["visitorBirthdayDay"])
            if not((birthdayMonth >= 1) and (birthdayMonth <= maxDate)):
                return renderTemplate("00003.html", daysUntil = False)
        except ValueError:
            return renderTemplate("00003.html", daysUntil = False)
        birthdayDate = datetime(today.year, birthdayMonth, birthdayDay)
        daysUntil = birthdayDate - today
        if daysUntil.days < 0:
            birthdayDate = datetime((today.year + 1), birthdayMonth, birthdayDay)
            daysUntil = birthdayDate - today
        daysUntilString = str(daysUntil.days + 1)
    else:
        return renderTemplate("00003.html", daysUntil = False)
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

@myApp.route("/functions/chatroom", methods = ["POST", "GET"])
def chatroom():
    chatroomHistory = chatroomMessageHistoryFile2List()
    if requestVariable.method == "POST":
        visitorName = requestVariable.form["visitorName"]
        visitorIP = requestVariable.remote_addr
        visitorMessageText = requestVariable.form["visitorMessage"]
        if visitorMessageText:
            try:
                visitorMessage = Message(visitorName, visitorIP, visitorMessageText)
                if not(checkSpam(visitorMessage)):
                    with open(chatroomHistoryDirection, "a") as chatroomHistoryFile:
                        chatroomHistoryFile.write(visitorMessage.getFormattedMessage())
            except ValueError:
                return renderTemplate("00004.html", historyChat = chatroomHistory, invalidInput = True)
    else:
        return renderTemplate("00004.html", historyChat = chatroomHistory, invalidInput = "")
    return renderTemplate("00004.html", historyChat = chatroomHistory, invalidInput = False)

#@myApp.route("/functions/form")
#def formFunction():
#    return renderTemplate("hello_submit_form.html")

# Main

if __name__ == '__main__':
    #print(chatroomMessageHistoryFile2List())
    myApp.run(host="0.0.0.0", port=80, debug=True)