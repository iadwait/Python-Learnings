name = input("Enter you name:")
age = int(input("Enter your age:"))

if age >= 18:
    print(f"Hello {name}, you are an adult!")
else:
    print(f"Hello {name}, you are a minor!")

print("\nCountdown from 5:")
for i in range(5,0,-1):
    print(f"Value if i = {i}")

print("Done !!")