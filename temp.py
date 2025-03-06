myDict = {}

target = 5

for i in range(10):
    myDict[str(i)] = eval(f"target == {i}")

print(myDict)