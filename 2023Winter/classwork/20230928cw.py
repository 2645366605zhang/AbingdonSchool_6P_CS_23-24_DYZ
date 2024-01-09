import re

text = "Rain in Spain is pain"

for match in (re.finditer("in", text)): # re.finditer("expression", "subjectString"), re.match("expression", "subjectString"), re.findall("expression", "subjectString"), re.search("expression", "subjectString")
    print(match.span()) # .span(), .string(), .group()

print(re.search("[a-zA-Z]{4}", text)) # Find any 4-letter-word

print(re.search("[A-Z][a-z]{4}", text)) # Find any 4-letter-word starting with a capital letter

crnMatch = (re.search("^[A-Z]{2}[0-9]{2} [A-Z]{3}", input("Enter a car registeration number.")))
#print(crnMatch)
if crnMatch is None: # Match only car registeration numbers
    print("This is not a CRN.")
else:
    print("This is a CRN.")

numMatch = (re.search("^[0-9]{3},[0-9]{3}.[0-9][1-9]$", input("Enter a number.")))
if numMatch is None: # Match numbers like: 111,222.33 or 999,888.77
    print("This is not a proper number.")
else:
    print("This is a proper number.")

def numberValidation():
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
    ]
    # TBD in hw