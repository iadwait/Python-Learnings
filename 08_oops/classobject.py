class Employee:
    def __init__(self, name, role): # __init__ - magical methods in python uses __METHODNAME__, mostly they are the inbuilt methods.
        self.name = name
        self.role = role

    def showInfo(self):
        print(f"Name = {self.name}, Role = {self.role}")


emp1 = Employee("Adwait", "Developer")
emp2 = Employee("john", "Tester")

emp1.showInfo()
emp2.showInfo()