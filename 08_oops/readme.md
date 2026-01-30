
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
