# Inheritance Demo with Menu

# ---------- Single Inheritance ----------
class SingleParent:
    def greet(self):
        print("Single Inheritance: Hello from Parent")
    
class SingleChild(SingleParent):
    pass


# ---------- Multiple Inheritance ----------
class MultiParent1:
    def greet1(self):
        print("Multiple Inheritance: Hello from Parent 1")

class MultiParent2:
    def greet2(self):
        print("Multiple Inheritance: Hello from Parent 2")

class MultiChild(MultiParent1, MultiParent2):
    pass

# ---------- Multilevel Inheritance ----------
class Grandparent:
    def greet(self):
        print("Multilevel Inheritance - Hello from Grandparent")
    
class Parent(Grandparent):
    def greet(self):
        print("Multilevel Inheritance - Hello from Parent")

class Child(Parent):
    pass

# ---------- Hierarchical Inheritance ----------
class HierParent:
    def greet(self):
        print("Hierarchical Inheritance - Hello from Parent")
    
class HierChild1(HierParent):
    pass

class HierChild2(HierParent):
    pass

# ---------- Hybrid Inheritance ----------
class A:
    def a(self):
        print("Hybrid Inheritance: A")


class B(A):
    def b(self):
        print("Hybrid Inheritance: B")

class C(A):
    def c(self):
        print("Hybrid Inheritance: C")

class D(B, C):
    pass        

# ---------- Menu ----------
while True:
    print("\n--- Inheritance Demo ---")
    print("1. Single Inheritance")
    print("2. Multiple Inheritance")
    print("3. Multilevel Inheritance")
    print("4. Hierarchical Inheritance")
    print("5. Hybrid Inheritance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        obj = SingleChild()
        obj.greet()

    elif choice == '2':
        obj = MultiChild()
        obj.greet1()
        obj.greet2()

    elif choice == '3':
        obj = Child()
        obj.greet()  # Calls Parent's greet (overrides Grandparent)

    elif choice == '4':
        obj1 = HierChild1()
        obj2 = HierChild2()
        obj1.greet()
        obj2.greet()

    elif choice == '5':
        obj = D()
        obj.a()
        obj.b()
        obj.c()

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid Choice! Try again.")