import re

"""

with open("sgyy.txt", "r", encoding = "utf8") as text:
    matches = re.finditer("刘备", text.read())
    #matches = re.finditer("([.]) ([\w,; ]+)+ (Dracula) ([\w,; ]+)+[.]", text.read())
    count = 0
    for match in matches:
        count += 1
        print(f"\nFound {match.group()} between characters: {match.span()}.")
    print(f'\n{count} "{match.group()}" found.')

"""

with open("dracula.txt", "r") as text:
    matches = re.finditer("([^.?!] )([A-Z]\w+)", text.read())
    count = 0
    for match in matches:
        count += 1
        print(f"\nFound {match.group()} between characters: {match.span()}.")
    print(f'\n{count} target(s) found.')

