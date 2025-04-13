## 📁 Project Setup

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/vadhiraj-kv/Fast-api.git
cd Fast-api
```

### 🐍 2. Create and Activate Virtual Environment

#### ➤ Create a Virtual Environment

```bash
python -m venv .venv
```

#### ➤ Activate the Environment

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

---

### 📦 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## 🚦 Run the FastAPI Server

Start the development server using:

```bash
uvicorn [filename]:app --reload
```

> ✅ Replace `[filename]` with your actual Python file name (without `.py` extension).

**Example:**
```bash
uvicorn cars:app --reload
```

---

## 🔍 API Documentation

Once the server is running, explore the auto-generated docs:

- 🌐 **Swagger UI**: http://127.0.0.1:8000/docs  

---

## 🧪 Optional: Freeze and Install Requirements

To save current dependencies:

```bash
pip freeze > requirements.txt
```
To install from the list:

```bash
pip install -r requirements.txt
```
---
## 📄 License
This project is licensed under the [MIT License](LICENSE).
---
> ✨ Happy Coding!
