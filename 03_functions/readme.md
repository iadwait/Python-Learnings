**Sr. No. 3: Functions (Short & Clear)**

Functions let you **group code into reusable blocks**.

---

### 1️⃣ Defining a Function

```python
def greet():
    print("Hello, Python!")
```

* `def` → keyword to define a function
* `greet` → function name
* `()` → can pass inputs (parameters)
* Code inside → **indented**

---

### 2️⃣ Calling a Function

```python
greet()  # Output: Hello, Python!
```

* Defining does nothing until you **call** it

---

### 3️⃣ Parameters & Arguments

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Adwait")  # Output: Hello, Adwait!
```

* **Parameter** → variable in function definition (`name`)
* **Argument** → value passed when calling the function (`"Adwait"`)

---

### 4️⃣ Return Statement

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

* `return` → sends a value back to where the function was called
* Functions **without return** return `None` by default

---

### ✅ Outcome

* Write **reusable, organized code**
* Pass data in & out of functions
* Avoid repeating code

---