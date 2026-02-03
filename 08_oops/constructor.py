# We can only have 1 init method in a class that can handle either default / parameterised constructor
class Test:
    def __init__(self, num1=None, num2=None):
        if num1 is None:
            num1 = 0
        if num2 is None:
            num2 = 0
        self.num1 = num1
        self.num2 = num2
        print(f"Value of Num1 = {num1}, Num2 = {num2}")


    # def __init__(self):
    #     print("Object Created")

    # def __init__(self, num1, num2):
    #     self.num1 = num1
    #     self.num2 = num2
    #     print("Values initialized for num1 and num2")


    
obj = Test()
obj = Test(2)
obj = Test(3,4)