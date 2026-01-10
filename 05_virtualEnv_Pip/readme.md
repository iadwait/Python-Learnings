## Sr. No. 5 – Virtual Environment & Pip

### 1. Virtual Environment (`venv`)

* Creates an **isolated Python environment** for each project.
* Keeps dependencies separate from global Python.
* **Create environment:**

```bash
# Windows
python -m venv myenv

# Mac/Linux
python3 -m venv myenv
```

* **Activate environment:**

```bash
# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```

### 2. Pip (Python Package Installer)

* Installs Python libraries/packages.

```bash
pip install <package_name>
```

### 3. requirements.txt

* Lists all project dependencies.
* **Save current packages:**

```bash
pip freeze > requirements.txt
```

* **Install from file:**

```bash
pip install -r requirements.txt
```

### ✅ Outcome

* **Clean, reproducible project setup**
* Easy to share and run projects without conflicts.

---