**Sr. No. 2: Data Structures (Short & Clear)**

Python has **4 main built-in data structures** you’ll use everywhere:

---

### 1️⃣ List

* Ordered, changeable collection
* Allows duplicates

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")   # add
print(fruits[1])          # access second item → banana
```

---

### 2️⃣ Tuple

* Ordered, **unchangeable** (immutable)
* Allows duplicates

```python
coordinates = (10, 20)
print(coordinates[0])    # 10
# coordinates[0] = 15 → ❌ error
```

---

### 3️⃣ Set

* Unordered, **unique elements only**

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)   # {1, 2, 3, 4} → duplicate removed
numbers.add(5)   # add element
```

---

### 4️⃣ Dictionary (dict)

* Key-value pairs
* Unordered, changeable

```python
person = {"name": "Adwait", "age": 25}
print(person["name"])     # Adwait
person["age"] = 26        # update value
person["city"] = "Pune"   # add new key-value
```

---
**these symbols are predefined in Python** and you **cannot change them**.

Here’s the breakdown:

| Data Structure | Symbol | Notes                      |
| -------------- | ------ | -------------------------- |
| List           | `[]`   | Ordered, mutable           |
| Tuple          | `()`   | Ordered, immutable         |
| Set            | `{}`   | Unordered, unique values   |
| Dictionary     | `{}`   | Unordered, key-value pairs |

**Important detail:**

* Both **Set** and **Dict** use `{}`, but Python knows the difference by **how you define it**:

```python
s = {1, 2, 3}        # Set
d = {"a": 1, "b": 2} # Dictionary
```

* You **cannot use `[]` for dicts** or `()` for lists — Python will throw an error.

---

### ✅ Outcome

* You can **store, access, and modify collections of data**
* Know which type fits your data best

---