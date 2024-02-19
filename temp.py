# Imports

import math as 数学

# Global Variables

陽 = True
陰 = False

# Functions

def 整数化(オブジェクト: str | float) -> int:
    return int(オブジェクト)

def 長さを返す(オブジェクト) -> int:
    return len(オブジェクト)

def 素数かどうかを確認する(数字: int) -> bool:
    素数 = 陽
    if 数字 <= 1:
        return (素数)
    else:
        for 係数 in range(2, 整数化(数学.sqrt(数字) + 1)):
            if 数字 % 係数 == 0:
                素数 = 陰
                break
    return (素数)

def 範囲内の素数を表示する(下限: int, 上限: int) -> list:
    素数リスト = []
    for 数字 in range(下限, 上限):
        if 素数かどうかを確認する(数字):
            素数リスト.append(数字)
    return (素数リスト)

def エラトステネスのふるい(上限: int) -> list:
    素数ブール値リスト = [陽 for 回数 in range(上限 + 1)]
    次の素数 = 2
    while((次の素数 ** 2) < 上限):
        if 素数ブール値リスト[次の素数]:
            for インデックス in range(次の素数 ** 2, 上限 + 1, 次の素数):
                素数ブール値リスト[インデックス] = 陰
        次の素数 += 1
    return (素数ブール値リスト)

def エラトステネスのふるいを表示する(素数ブール値リスト: list):
    for 数字 in range(2, 長さを返す(素数ブール値リスト)):
        if 素数ブール値リスト[数字]:
            print(数字)

# Main

"""while 陽:
    userInput = input("Please enter an integer: ")
    print(素数かどうかを確認する(整数化(userInput)))
    if input('Do you want to stop?\nEnter "No" to stop, press Enter to continue.\n').lower() == "no":
        break"""

"""for 数字 in 範囲内の素数を表示する(0, 10000000):
    print(数字)"""
if __name__ == "__main__":
    エラトステネスのふるいを表示する(エラトステネスのふるい(10000000))
