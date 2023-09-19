#Dictionaries

soundDict = {"Cat":"Meow", "Dog":"Woof", "Trump":"China"} # Keys and values can be in many different data types. Key is constant, and value can be changed.
numDict = {"Trump":1, "Cat":14, "Dog":513}

def showSound():
    for animal in soundDict:
        print(f"{animal}: {soundDict[animal]}")
    print("\n")

def showNum():
    for animal in numDict:
        print(f"There are {numDict[animal]} {animal}(s).")
    print("\n")

showSound()

soundDict["Cat"] = "Purr" # Reassign value to a key.
soundDict["Cow"] = "Moo" # Create a new key, which looks the same as line 11.

showSound()

#print(soundDict["Donkey"]) # This will return an error
print(soundDict.get("Donkey")) # Same action with line 17, but will return "None".
print(soundDict.get("Donkey", "Huh?")) # Will look for the value for the first key("Donkey" here for example), if not found, return the default value after it. 

numDict["Dog"] += 1 # You can manipulate values in a dictionary just like items in a list

showNum()