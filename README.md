# 🚀 StockFlowAPI

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,100:1e293b&height=200&section=header&text=StockFlowAPI&fontSize=40&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <b>Full-Stack Inventory Management System</b><br>
  Built with FastAPI ⚡ PostgreSQL 🐘 SQLAlchemy 🧠 React ⚛️
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0ea5e9?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

## 📸 Project Preview

<p align="center">
  <img src="./frontend/screenshots/demo.png" width="80%"/>
</p>

# 🚀 StockFlowAPI

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,100:1e293b&height=200&section=header&text=StockFlowAPI&fontSize=40&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <b>Secure Full-Stack Inventory Management System</b><br>
  Built with FastAPI ⚡ PostgreSQL 🐘 SQLAlchemy 🧠 React ⚛️ JWT 🔐
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0ea5e9?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/JWT-Auth-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

## ⚡ Features

* 🔐 JWT Authentication (Login & Register)
* 🛡️ Protected API routes
* 📦 Full CRUD operations on products
* ⚡ FastAPI high-performance backend
* 🐘 PostgreSQL database integration
* 🧠 SQLAlchemy ORM
* ✅ Pydantic validation
* ⚛️ React frontend with modern UI
* 🎨 Clean and responsive UI (Auth + Dashboard)
* 🔎 Search, filter & sort products
* 🔄 Real-time UI updates after CRUD
* 🌐 Deployed backend (Render)

---

## 🧠 Tech Stack

**Backend:**
FastAPI, SQLAlchemy, PostgreSQL, Pydantic, Uvicorn, JWT Authentication

**Frontend:**
React (Vite), Axios, CSS (custom UI), LocalStorage (Auth state)

---

## 📁 Project Structure

```
StockFlowAPI
├── backend
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── auth.py
│   ├── routes/
│   ├── .env (ignored)
│
├── frontend
│   ├── src
│   │   ├── components (Login, Register)
│   │   ├── api.js
│   │   ├── App.js
│   │   ├── App.css
│   ├── public
│   ├── package.json
│
└── README.md
```

---

## 🚀 API Endpoints

### 🔐 Auth

* `POST /register` → Register user
* `POST /login` → Login & get JWT token

### 📦 Products (Protected)

* `GET /products` → Get all products
* `GET /products/{id}` → Get product by id
* `POST /products` → Add product
* `PUT /products/{id}` → Update product
* `DELETE /products/{id}` → Delete product

---

## ⚙️ Setup Instructions

### 🔹 Clone repo

```
git clone https://github.com/your-username/StockFlowAPI.git
cd StockFlowAPI
```

---

### 🔹 Backend setup

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/stockflow
SECRET_KEY=your_secret_key
```

Run backend

```
uvicorn main:app --reload
```

Backend → http://127.0.0.1:8000
Docs → http://127.0.0.1:8000/docs

---

### 🔹 Frontend setup

```
cd frontend
npm install
npm run dev
```

Frontend → http://localhost:3000

---

## 🔐 Authentication Flow

1. User registers → credentials stored securely
2. User logs in → receives JWT token
3. Token stored in localStorage
4. Token sent with API requests
5. Protected routes validate token

---

## 🧠 Learnings

* 🔐 Implemented JWT authentication in FastAPI
* ⚡ Built scalable REST APIs with proper structure
* 🐘 Integrated PostgreSQL with SQLAlchemy ORM
* 🔗 Connected React frontend with secured backend
* 🎨 Designed modern UI with clean UX
* 🐞 Debugged real-world deployment & CORS issues
* 🚀 Managed full-stack project deployment

---

## 👨‍💻 Author

**Amaan Shikalgar**
Full Stack Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

