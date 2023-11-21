class 货车():

    def __init__(self, 拥有者: str, 重量: float, 轮数: int):
        self._拥有者 = 拥有者
        self._重量 = 重量
        self._轮数 = 轮数
    
    def 获取拥有者(self):
        return self._拥有者
    
    def 获取重量(self):
        return self._重量
    
    def 获取轮数(self):
        return self._轮数

class 开放式货车(货车):
    pass

class 封闭式货车(货车):

    def __init__(self, 拥有者: str, 重量: float, 高: float, 轮数: int, 门数: int, 是否适合食品: bool):
        self._拥有者 = 拥有者
        self._重量 = 重量
        self._高 = 高
        self._轮数 = 轮数
        self._门数 = 门数
        self._是否适合食品 = 是否适合食品
    
    def 获取高(self):
        return self._高
    
    def 获取门数(self):
        return self._门数
    
    def 获取是否适合食品(self):
        return self._是否适合食品

class 轨道():

    def __init__(self):
        self._货车 = [None] * 30
        self._栈顶指针 = -1
    
    def 是否为空(self):
        return (self._栈顶指针 == -1)

    def 是否为满(self):
        return (self._栈顶指针 == 29)

    def 入栈(self, 入栈货车: 货车):
        if not(self.是否为满()):
            self._栈顶指针 += 1
            self._货车[self._栈顶指针] = 入栈货车
        else:
            raise Exception("轨道已满，入栈操作失败")

    def 出栈(self):
        if not(self.是否为空()):
            出栈货车 = self._货车[self._栈顶指针]
            self._货车[self._栈顶指针] = None
            self._栈顶指针 -= 1
            return 出栈货车
        else:
            raise Exception("轨道为空，出栈操作失败")
    
    def 查看栈顶(self):
        if self.是否为空():
            return None
        else:
            return (self._货车[self._栈顶指针])

class 货车站():
    
    def __init__(self, 轨道数量: int):
        self._轨道数量 = 轨道数量
        self._轨道 = [轨道()] * 轨道数量
    
    def 进入货车(self, 轨道ID: int, 入站货车: 货车):
        if 轨道ID < len(self._轨道):
            self._轨道[轨道ID].入栈(入站货车)
        else:
            raise Exception("无效轨道ID，进入货车操作失败")
    
    def 移出货车(self, 轨道ID: int):
        if 轨道ID < len(self._轨道):
            return self._轨道[轨道ID].出栈()
        else:
            raise Exception("无效轨道ID，移出货车操作失败")
    
    def 查看货车(self, 轨道ID: int):
        if 轨道ID < len(self._轨道):
            return self._轨道[轨道ID].查看栈顶()
        else:
            raise Exception("无效轨道ID，查看货车操作失败")
    
    def 检查所有货车(self, 轨道ID: int):
        if 轨道ID < len(self._轨道):
            for 货车 in self._轨道[轨道ID]._货车:
                if not(货车 == None):
                    print(货车.获取拥有者())
        else:
            raise Exception("无效轨道ID，检查所有货车操作失败")

if __name__ == "__main__":
    testYard = 货车站(5)
    testYard.进入货车(0, 开放式货车("詹姆斯·G", 3.0, 12))
    testYard.进入货车(0, 开放式货车("詹姆斯·I", 2.0, 9))
    testYard.进入货车(0, 封闭式货车("詹姆斯·管", 2.0, 10.0, 16, 4, True))
    for i in range(27):
        testYard.进入货车(0, 开放式货车(f"占位符{i}", 5.5, 6))
    #testYard.addWagon(0, Wagon("PLACEHOLDER114514", 2.0, 12)) # This will raise an exception as the sliding is full
    for i in range(30):
        print(testYard.移出货车(0).获取拥有者())
    #testYard.removeWagon(1) # This will raise an exception as sliding 1 in yard testYard is empty