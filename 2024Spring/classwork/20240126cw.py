from itertools import permutations

def getPermutationList(objectList: list) -> list:
    permutationList = []
    if len(objectList) <= 1:
        return [objectList]
    for itemIndex in range(len(objectList)):
        for permutation in getPermutationList(objectList[:itemIndex] + objectList[(itemIndex + 1):]):
            permutationList.append([objectList[itemIndex]] + permutation)
    return permutationList

if __name__ == "__main__":
    #print(getPermutationList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    #print(list(permutations(list(range(0, 10)))))

    for permutation in permutations("saippuakivikauppias"):
        if permutation == "saippuakivikauppias":
            print(permutation)