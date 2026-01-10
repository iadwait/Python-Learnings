**Sr. No. 4: File Handling (Short & Clear)**

Python allows you to **read and write files**, so you can **store data permanently**.

---

### 1️⃣ Writing to a File

```python
# Open file in write mode ('w') - creates file if not exists
file = open("example.txt", "w")
file.write("Hello, Python!\n")
file.write("Learning file handling is fun!")
file.close()  # Always close the file
```

* Modes:

  * `'w'` → write (overwrite)
  * `'a'` → append
  * `'r'` → read

---

### 2️⃣ Reading from a File

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

* `.read()` → reads entire file
* `.readline()` → reads line by line

---

### 3️⃣ Using `with` (Better Practice)

```python
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())  # removes extra newline
```

* `with` automatically **closes the file** after the block

---

### 4️⃣ Working with JSON

```python
import json

data = {"name": "Adwait", "age": 25}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

* JSON = structured data format for saving **dict-like data**

---

### ✅ Outcome

* Save and retrieve data from **text files & JSON**
* Use `with` for safer file handling
* Understand reading, writing, appending, and structured storage

---