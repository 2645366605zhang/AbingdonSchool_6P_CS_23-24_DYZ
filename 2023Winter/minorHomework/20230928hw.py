import re

tests = [
("114,514.19", True), 
("191,981.0", False), 
("sd.kfz.111", False), 
("255.255.255.0", False), 
("222,333.44", True), 
("Number", False), 
("CA985", False), 
("914,154.11", True), 
("Don,ald.Tr", False), 
("pro,per.nm", False), 
("1,056.12", True), 
("56.78", True), 
("123,456.78", True), 
("21,000,000.12", True), 
("1056.26", False), 
("1,000,000.120", False), 
("123,15.45", False), 
]

#print(re.search("^[1-9]{1}([0-9]{1})?([0-9]{1})?(,[0-9]{3})*.[0-9][1-9]$", input("Input: ")))

def reTest(testList):
    for test in testList:
        numMatch = (re.search("^[1-9]{1}([0-9]{1})?([0-9]{1})?(,[0-9]{3})*.[0-9][1-9]$", test[0]))
        if numMatch == None:
            result = "Fail"
        else:
            result = "Pass"    
        if test[1]:
            target = "Pass"
        else:
            target = "Fail"
        if target == result:
            validity = "Success"
        else:
            validity = "Failure"
        print(f'\nTest item "{test}" is expected to return {target}, actually returned {result}.\nThis test is a {validity}.')

reTest(tests)