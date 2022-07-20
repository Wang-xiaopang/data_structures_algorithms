"""
UML图
类：ArithmeticProgression，等差数列
域：_start _ increment
行为:increment()
"""
class ArithmeticProgression:
    """创建等差"""
    def __init__(self,increment,start=0,length = 1):
        """
        创建等差数列的实例
        start:开始值
        increment:差值
        length:期望数列的长度
        end:最后结果
        """
        self._start = start
        self._increment = increment
        self._end = [start]
        self._length = length

    def increment(self):
        """返回数组结果"""
        while True:
            if len(self._end) == self._length:
                break
            self._start += self._increment
            self._end.append(self._start)
        return self._end

if __name__ == '__main__':
    a = ArithmeticProgression(3,1,153)
    print(a.increment())

