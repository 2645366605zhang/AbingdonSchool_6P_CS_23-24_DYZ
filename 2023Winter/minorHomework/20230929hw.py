integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

tests = [
("A114 514", False), 
("AB12 CDE", True), 
("OX14 1DE", False), 
("aCar Reg", False), 
('"A random string"', False), 
("1919 810", False), 
("RC66 PAS", True), 
("MP40 666", False), 
("HK99 ACS", True), 
("LD29 QFW", True), 
("SG16 RVE", True), 
("ab12 cde", False)
]

def checkCarReg(carReg):
    carRegCharIndex = 0
    for char in str(carReg):
        validCarReg = False
        #print(f"CRCI is now: {carRegCharIndex}, current character is {char}")
        if (carRegCharIndex in range(2)) and (char in upperLetters):
            validCarReg = True
            #print("Pass test section 0")
        elif (carRegCharIndex in range(2, 4)) and (char in integers):
            validCarReg = True
            #print("Pass test section 1")
        elif (carRegCharIndex == 4) and (char == " "):
            validCarReg = True
            #print("Pass test section 2")
        elif (carRegCharIndex in range(5, 8)) and (char in upperLetters):
            validCarReg = True
            #print("Pass test section 3")
        carRegCharIndex += 1
        if not(validCarReg):
            #print(f"Test failed at CRCI = {carRegCharIndex}, current character is {char}")
            break
        elif carRegCharIndex == 8:
            #print("Fully pass test")
            break
    return validCarReg

def reTest(testList):
    for test in testList:
        if checkCarReg(test[0]) == test[1]:
            result = "Success"
        else:
            result = "Failure"
        print(f'\nTest item "{test[0]}" is expected to return {test[1]}, actually returned {checkCarReg(test[0])}.\nThis test is a {result}.')

reTest(tests)