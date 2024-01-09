import random as suiJi

Yang = True
Yin = False
Wu = None

def changDu(muBiao):
    return len(muBiao)

def daYin(muBiao):
    print(muBiao)

def erJinZhiDongWuJianSuo(shuJvLieBiao, muBiao):
    weiFaXianMuBiao = Yang
    jieGuo = [Yin, Wu]
    dingBuZhiZhen = 0
    diBuZhiZhen = (changDu(shuJvLieBiao) - 1)
    zhongJianZhiZhen = (dingBuZhiZhen + ((diBuZhiZhen - dingBuZhiZhen) // 2))
    while weiFaXianMuBiao:
        #daYin(f"topP: {dingBuZhiZhen}\nendP: {diBuZhiZhen}\nmidP: {zhongJianZhiZhen}\n") # Debug
        if shuJvLieBiao[zhongJianZhiZhen] == muBiao:
            weiFaXianMuBiao = Yin
            jieGuo = [Yang, zhongJianZhiZhen]
        elif zhongJianZhiZhen == dingBuZhiZhen:
            break
        else:
            ziMuSuoYin = 0
            shuJvDaYvMuBiao = Yin
            for ziMu in shuJvLieBiao[zhongJianZhiZhen]:
                if ziMu > muBiao[ziMuSuoYin]:
                    break
                elif ziMu < muBiao[ziMuSuoYin]:
                    shuJvDaYvMuBiao = Yang
                    break
                ziMuSuoYin += 1
            if shuJvDaYvMuBiao:
                dingBuZhiZhen = zhongJianZhiZhen
                zhongJianZhiZhen = (dingBuZhiZhen + ((diBuZhiZhen - dingBuZhiZhen) // 2))
            else:
                diBuZhiZhen = zhongJianZhiZhen
                zhongJianZhiZhen = (dingBuZhiZhen + ((diBuZhiZhen - dingBuZhiZhen) // 2))
    return jieGuo

myAnimalList = ["alligator", "bee", "cat", "dog", "elephant", "fish", "gazelle", "grasshopper", "hippopotamus", "horse", "hyena", "iguana", "jaguar", "jellyfish"]
randomAnimal = myAnimalList[suiJi.randint(0, (changDu(myAnimalList) - 1))]
daYin(f"\nAnimal: {randomAnimal}\nResult: {erJinZhiDongWuJianSuo(myAnimalList, randomAnimal)}\n")