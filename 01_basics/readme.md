**Sr. No. 1: Python Basics (Short & Clear)**

**Topics:** Variables, Data Types, Loops, Conditions

---

### 1️⃣ Variables

* Store data values.
* No declaration needed; just assign:

```python
x = 10      # integer
name = "Adwait"  # string
pi = 3.14   # float
```

---

### 2️⃣ Data Types

* **int** → whole numbers
* **float** → decimals
* **str** → text
* **bool** → True/False

```python
is_active = True
age = 25
```

---

### 3️⃣ Conditions (if-else)

* Make decisions

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

### 4️⃣ Loops

* Repeat actions
* **for loop** → iterate over items

```python
for i in range(3):
    print(i)
```

* **while loop** → repeat while condition is True

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

---

### ✅ Outcome

* You can **write basic Python programs**
* Understand how data is stored and controlled

---


Ways to print in python 

Using f vs without using f
name = "Adwait"
age = 20

# Without f-string
print("Hello " + name + ", you are " + str(age) + " years old.")

# With f-string
print(f"Hello {name}, you are {age} years old.")