from __future__ import annotations
import random

def merge(list0: list, list1: list, targetList: list):
    list0Pointer = 0
    list1Pointer = 0
    while (list0Pointer + list1Pointer) < len(targetList):
        if (list1Pointer == len(list1)) or ((list0Pointer < len(list0)) and (list0[list0Pointer] < list1[list1Pointer])):
            targetList[list0Pointer + list1Pointer] = list0[list0Pointer]
            list0Pointer += 1
        else:
            targetList[list0Pointer + list1Pointer] = list1[list1Pointer]
            list1Pointer += 1
    return targetList

def mergeSort(targetList: list):
    listLength = len(targetList)
    if listLength < 2:
        return None
    listMidpoint = listLength // 2
    headList = targetList[0:listMidpoint]
    tailList = targetList[listMidpoint:listLength]
    mergeSort(headList)
    mergeSort(tailList)
    merge(headList, tailList, targetList)
    return targetList

if __name__ == "__main__":
    testList = []
    for i in range(10000):
        testList.append(random.randint(0, 100))
    print(mergeSort(testList))