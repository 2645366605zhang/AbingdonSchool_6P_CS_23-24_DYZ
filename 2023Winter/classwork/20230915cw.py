from sys import getsizeof

testList = [114514, "114514", [1, 14, 514], True]

for object in testList:
    print(f"\n{object}'s type is {type(object)}, with size of {getsizeof(object)} bytes.")