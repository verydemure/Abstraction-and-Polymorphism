from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self,x):
        print("passed value", x)

    # Abstract Method
    @abstractmethod
    def task(self):
        print("we are in the Absclass task")


class testClass(Absclass):
    def task(self):
        print("we are inside test_class task")


testObj = testClass()
testObj.task()

testObj.print(100)
