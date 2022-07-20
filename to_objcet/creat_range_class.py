"""
UML图：
类：创建一个Range类，返回长度
域:_start _end _step _length
行为:start() end() step() length()
"""

class Range:
    """创建一个返回range长度的类"""
    def __init__(self,start,end=None,step=0):
        self._start = start
        self._end = end
        self._step = step
        self._length = 1

    def start(self):
        """返回开始的值"""
        return self._start

    def end(self):
        """返回结束的值"""
        if self._end < self.start():
            print('end的值太小了，变成开始值哦')
            self._end = self.start()
        elif self._end == None:
            self._end = self.start()
            self._start = 0
        return self._end
    def step(self):
        """返回步长"""
        if self._step == 0:
            self._step = 1
        return self._step

    def length(self):
        self._length += self.end()-self.start()//self.step()
        return self._length


if __name__ == '__main__':
    a = Range(1,3)
    print(a.length())



