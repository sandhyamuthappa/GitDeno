from constructors import calculator

class childimp(calculator):
    num2=34
    def __init__(self):
        calculator.__init__(self, 4,5)

    def getcomp(self):
        return self.num + self.num2 + self.summation()


obj=childimp()
print(obj.getcomp())

