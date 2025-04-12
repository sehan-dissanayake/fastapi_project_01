# FastAPI Project

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### 🔁 Clone the Repository

### 🐍 Create & Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 Install Dependencies

Make sure you’re in the project root and the virtual environment is active:

```bash
pip install -r requirements.txt
```

---

### ▶️ Run the Server

If the entrypoint is `main.py`, use:

```bash
python main.py
```

Or using fastapi[strandard]:

```bash
fastapi dev main.py
```

**Or using uvicorn:**
```bash
uvicorn main:app --reload
```

The app will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 🧾 Generating requirements.txt (if you change dependencies)

If you add or update packages, regenerate the `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Commit it so everyone stays in sync.

---

### 📁 Notes

- The `venv/` folder is gitignored — each collaborator should create their own.
- Python 3.8+ is recommended (check version with `python --version`).