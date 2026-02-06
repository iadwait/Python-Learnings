class Example:
    public_var = 1
    _protected_var = 2
    __private_var = 3

    def public_method(self):
        print("Public method")
        # self.__private_method() # Accessing private method from other function inside a class

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

# Create object
obj = Example()

# Public
print(obj.public_var)      # 1
obj.public_method()        # Public method

# Protected
print(obj._protected_var)  # 2 (works, but discouraged)
obj._protected_method()    # Protected method (works, discouraged)

# Private
# print(obj.__private_var)   # ❌ Error
# obj.__private_method()     # ❌ Error

# Access private via name mangling
print(obj._Example__private_var)  # 3
obj._Example__private_method()    # Private method
