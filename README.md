# 🚀 StockFlowAPI (Full Stack)

A full-stack web application built using **FastAPI**, **PostgreSQL**, and a frontend interface.
This project demonstrates CRUD operations, API design, database integration, and full-stack development.

---

## 📌 Features

* 🔹 RESTful API with FastAPI
* 🔹 CRUD operations (Create, Read, Update, Delete)
* 🔹 Data validation using Pydantic
* 🔹 PostgreSQL integration with SQLAlchemy
* 🔹 Full-stack setup (Frontend + Backend)
* 🔹 Interactive API docs (Swagger UI)
* 🔹 Clean and modular project structure

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn

### Frontend

* (Add your frontend tech here: React / HTML-CSS-JS)

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/AmaanShikalgar/fastapi-product-api.git
cd fastapi-product-api
```

---

### 2. Backend Setup

```bash
cd backend   # if backend folder exists
python -m venv myenv
myenv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

### 3. Configure Database

Update your database URL in `database.py`:

```python
db_url = "postgresql://postgres:yourpassword@127.0.0.1:5432/mydb"
```

> Make sure PostgreSQL is running and the database exists.

---

### 4. Run Backend Server

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### 5. Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 📂 Project Structure

```
fastapi-product-api/
│── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│
│── frontend/
│   ├── src/
│   ├── public/
│
│── requirements.txt
│── .gitignore
│── README.md
```

---

## 🔗 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /products      | Get all products  |
| GET    | /products/{id} | Get product by ID |
| POST   | /products      | Create product    |
| PUT    | /products/{id} | Update product    |
| DELETE | /products/{id} | Delete product    |

---

## 🧠 Learnings

* Built REST APIs using FastAPI
* Implemented ORM with SQLAlchemy
* Used Pydantic for data validation
* Integrated PostgreSQL database
* Connected frontend with backend APIs
* Debugged real-world backend issues (authentication, constraints, etc.)

---

## 🚀 Future Improvements

* Add JWT Authentication
* Implement pagination & filtering
* Dockerize the application
* Deploy using CI/CD pipelines

---

## 👨‍💻 Author

**Amaan Shikalgar**

* GitHub: https://github.com/AmaanShikalgar

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
