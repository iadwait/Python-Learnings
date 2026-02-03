# Method Overloading
class calc:
    def add(self, a, b, c=0):
        return a + b + c

c = calc()
print(f"{c.add(2, 3)}")
print(f"{c.add(2, 3, 4)}")

class calc2:
    def add(self, *args):
        total = 0
        for i in args:
            total += i
        return total
    
c = calc2()
print(f"{c.add(2, 3)}")
print(f"{c.add(2, 3, 4)}")
print(f"{c.add(1, 2, 3, 4)}")

# Method Overriding

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

def callShow(obj):
    obj.show()

callShow(Parent())
callShow(Child())