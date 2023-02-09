#

class calculator:
    num=100

    def __init__(self,a,b):
        self.first=a
        self.second=b

    def getdata(self):
        print("we are in python class")
    def summation(self):
        return self.first +self.second
obj=calculator(3,4)
obj.getdata()
print(obj.summation())