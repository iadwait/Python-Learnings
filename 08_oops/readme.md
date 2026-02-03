
---

### **1️⃣ Class & Object**

* **Class:** Blueprint defining **data members** and **member functions**.
* **Object:** Instance of a class that can use those **data members** and **member functions**.

**Purpose:** Organize related data and functions together into one unit.

---

### **2️⃣ Encapsulation**

* **Definition:** Wrapping **data members** and **member functions** into a single unit and **restricting direct access** to data members.
* **How:** Make data private, provide **member functions** (getters/setters) to access/modify.
* **Purpose:** Protect data from accidental changes, control access, and keep the class organized.

---

### **3️⃣ Abstraction**

* **Definition:** Showing only the **necessary member functions** to the user and **hiding implementation details**.
* **How:** Use **abstract classes** and **abstract methods**; subclasses implement the hidden logic.
* **Purpose:** Simplifies usage, hides complexity; user only sees public methods.
* **Key point:** Even if the object is of a subclass (e.g., `CreditCard`), the user calls only **superclass methods** like `pay()` and doesn’t see or need to know the internal implementation (`process_payment()`).

---

### **Difference Between Encapsulation & Abstraction**

| Feature           | Encapsulation                                                          | Abstraction                                                                      |
| ----------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **What it hides** | Data members (variables)                                               | Implementation of methods (how things work)                                      |
| **How it hides**  | Make data private + access via member functions                        | Use abstract methods/classes; subclass implements logic                          |
| **Purpose**       | Protects data from being changed directly and allows controlled access | Simplifies interface, hides internal details, reduces complexity                 |
| **Who sees it**   | Member functions in the class can access data                          | User sees only public methods; implementation is hidden even in subclass objects |

---

Here’s the **updated table and last notes** including the “without abstract method” case:

---

### **Notes**

* **ABC alone does not prevent object creation**
* **Only @abstractmethod makes the class truly abstract** and enforces that subclasses implement certain methods
* If an ABC has **no abstract methods**, you **can still create its object**

---

### **Summary Table**

| Thing                        | Without `@abstractmethod` | With `@abstractmethod`            |
| ---------------------------- | ------------------------- | --------------------------------- |
| Subclass implementation      | Optional                  | Mandatory                         |
| Can create Payment object?   | ✅ Yes                     | ❌ No                              |
| Does it enforce abstraction? | ❌ No                      | ✅ Yes                             |
| `pass` meaning               | Placeholder, does nothing | Same, but now required for syntax |

Here’s a **short, clear note** combining both points:

---

### **Abstract Method Call in Python**

* The **parent class abstract method is never called**; it only defines a **contract** that subclasses must implement.
* When the superclass calls:

```python
self.process_payment(amount)
```

* Python sees that `self` is a **subclass object**
* It **directly calls the subclass’s method**, not the parent’s
* There is **no call to the parent method then redirection** — the parent’s abstract method is just a placeholder.

✅ **Key point:** Abstract method = contract; actual execution = subclass implementation.

---

### Inheritance

### **1. Single Inheritance**

* One parent, one child.

```
Parent
  │
Child
```

* Child inherits all methods/attributes of Parent.

---

### **2. Multiple Inheritance**

* One child, multiple parents.

```
Parent1   Parent2
   \       /
     Child
```

* Child inherits from both Parent1 and Parent2.

---

### **3. Multilevel Inheritance**

* Chain of inheritance.

```
Grandparent
      │
   Parent
      │
    Child
```

* Methods can be overridden in any level.

---

### **4. Hierarchical Inheritance**

* One parent, multiple children.

```
     Parent
     /    \
Child1   Child2
```

* All children inherit from the same parent.

---

### **5. Hybrid Inheritance**

* Combination of two or more types (e.g., multiple + multilevel).

```
       A
      / \
     B   C
      \ /
       D
```

* D inherits from B and C, which both inherit from A.

---

Sure! Here’s a **complete, clean set of Python Polymorphism notes**, combining everything we discussed. Perfect for exam or revision:

---

# **Polymorphism in Python**

**Definition:**

* Polymorphism means **“one interface, many forms”**.
* Allows objects of **different classes** to be treated **uniformly**.
* Python supports two main types: **Method Overloading** and **Method Overriding**.

---

## **1. Method Overloading (Python way / Simulated)**

* **Definition:** Same method name, different parameters (number or type).
* **Python Note:** Python **does NOT support traditional method overloading**.

  * If multiple methods with the same name are defined in a class, **only the last one is used**.
* **How to achieve in Python:**

  * Use **default arguments**
  * Use **`*args`** to accept variable number of arguments
* **Important points:**

  * Same method name **cannot exist multiple times** in the class.
  * Overloading in Python is **simulated**, not true runtime polymorphism.
  * Python handles **different arguments inside the same method**.

---

## **2. Method Overriding (Runtime / Dynamic Polymorphism)**

* **Definition:** Child class provides its **own implementation** of a parent’s method.
* **Key feature:** **Python decides at runtime which method to execute**, based on the **actual object type**.
* **Important points:**

  * Python is **dynamically typed**, so method resolution happens **at runtime**.
  * Can use **`super()`** to call the parent class method inside child’s method.
  * Shows **true runtime polymorphism**.

---

## **Key Differences Between Overloading & Overriding**

| Feature            | Method Overloading (Python)                            | Method Overriding                                        |
| ------------------ | ------------------------------------------------------ | -------------------------------------------------------- |
| Method Name        | Same                                                   | Same                                                     |
| Parameters         | Different / optional / `*args`                         | Same as parent                                           |
| Class Involved     | Same class                                             | Parent & child class                                     |
| Runtime Decision   | ❌ Not runtime; handled **inside method** based on args | ✅ Runtime; Python chooses method based on object’s class |
| Use of `super()`   | Not applicable                                         | Can be used                                              |
| True Polymorphism? | No (simulated in Python)                               | Yes (runtime polymorphism)                               |

---

## **Summary**

* **Polymorphism = one interface, multiple behaviors**
* **Overloading** → handled using default args or `*args` (**simulated**)
* **Overriding** → dynamic method resolution (**true runtime polymorphism**)
* **Important:** Python only keeps the **last defined method** if method names clash

---

# **Constructor in Python**

### 1. What is a Constructor?

* A constructor is a special method used to **initialize an object** when it is created.
* In Python, the constructor is always:

```python
__init__(self, ...)
```

---

### 2. Key Points about `__init__`

* Each class can have **only one `__init__`** method.
* Python does **not support multiple constructors** like Java or C++.
* `__init__` is called **automatically** when an object is created.

---

### 3. Parameterized Constructor

* `__init__` can take parameters to initialize object attributes:

```python
class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = Test(10, 20)
```

---

### 4. Default Parameter Values

* Parameters can have **default values**:

```python
class Test:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

obj1 = Test()      # x=0, y=0
obj2 = Test(5, 10) # x=5, y=10
```

* This allows **optional parameters** and simulates multiple constructors.

---

### 5. Using `*args` and `**kwargs`

* For **variable number of arguments**, you can use:

```python
class Test:
    def __init__(self, *args, **kwargs):
        print(args, kwargs)

obj = Test(1, 2, 3, a=4, b=5)
```

* `*args` → tuple of positional arguments
* `**kwargs` → dictionary of keyword arguments

This is another way to **simulate multiple constructors**.

---

### 6. Alternative Constructor using `@classmethod`

* You can define **class methods** that create objects differently:

```python
class Test:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_sum(cls, a, b):
        return cls(a + b)

obj1 = Test(10)
obj2 = Test.from_sum(4, 6)  # value = 10
```

* `cls` refers to the class itself.
* The method **returns a new object**, acting like an **alternative constructor**.

---

### 7. Key Takeaways

* Python has **one constructor per class (`__init__`)**.
* You can **simulate multiple constructors** using:

  * Default parameters
  * `*args` and `**kwargs`
  * `@classmethod` alternative constructors
* Constructor is **called automatically** when the object is created.

* **`None` is a singleton object** — there is only **one `None` object** in memory.
* In `__init__`, if a parameter is **not passed**, Python assigns it the default value you wrote (`None` in this case).
* So **checking `param is None`** tells you: “The caller didn’t provide a value,” and you can then assign a real default like `0`.

It’s not that the parameter doesn’t exist in memory — it **exists**, but its value is the `None` object until you assign something else.

---

## **`*args` and `**kwargs` in Python**

### 1. `*args`

* Allows a function to accept **any number of positional arguments**.
* Stored as a **tuple**.

**Example:**

```python
def add_numbers(*args):
    print(args)  # tuple of all numbers
    print(sum(args))

add_numbers(1, 2, 3)  # Output: (1, 2, 3) → 6
```

---

### 2. `**kwargs`

* Allows a function to accept **any number of keyword arguments**.
* Stored as a **dictionary**.

**Example:**

```python
def print_info(**kwargs):
    print(kwargs)

print_info(name="Alice", age=25)  # Output: {'name': 'Alice', 'age': 25}
```

---

### 3. Combined Usage

```python
def func(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

func(1, 2, x=10, y=20)
# Output:
# Args: (1, 2)
# Kwargs: {'x': 10, 'y': 20}
```

---

✅ **Summary:**

* `*args` → variable **positional parameters** (tuple)
* `**kwargs` → variable **named parameters** (dictionary)

---