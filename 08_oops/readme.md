
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
