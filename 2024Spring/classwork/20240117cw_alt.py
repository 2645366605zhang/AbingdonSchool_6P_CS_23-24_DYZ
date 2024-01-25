# Imports

import math as 数学

# Global Variables

阳 = True
阴 = False

# Functions

def 整数化(对象: str | float) -> int:
    return int(对象)

def 返回长度(对象) -> int:
    return len(对象)

def 检查是否为质数(数字: int) -> bool:
    是质数 = 阳
    if 数字 <= 1:
        return (是质数)
    else:
        for 系数 in range(2, 整数化(数学.sqrt(数字) + 1)):
            if 数字 % 系数 == 0:
                是质数 = 阴
                break
    return (是质数)

def 显示之间的质数(下限: int, 上限: int) -> list:
    质数列表 = []
    for 数字 in range(下限, 上限):
        if 检查是否为质数(数字):
            质数列表.append(数字)
    return (质数列表)

def 埃拉托斯特尼筛法(上限: int) -> list:
    质数布尔值列表 = [阳 for 次数 in range(上限 + 1)]
    下一个质数 = 2
    while((下一个质数 ** 2) < 上限):
        if 质数布尔值列表[下一个质数]:
            for 索引 in range(下一个质数 ** 2, 上限 + 1, 下一个质数):
                质数布尔值列表[索引] = 阴
        下一个质数 += 1
    return (质数布尔值列表)

def 显示埃拉托斯特尼筛法(质数布尔值列表: list):
    for 数字 in range(2, 返回长度(质数布尔值列表)):
        if 质数布尔值列表[数字]:
            print(数字)

# Main

"""while 阳:
    userInput = input("Please enter an integer: ")
    print(检查是否为质数(整数化(userInput)))
    if input('Do you want to stop?\nEnter "No" to stop, press Enter to continue.\n').lower() == "no":
        break"""

"""for 数字 in 显示之间的质数(0, 10000000):
    print(数字)"""
if __name__ == "__main__":
    显示埃拉托斯特尼筛法(埃拉托斯特尼筛法(10000000))