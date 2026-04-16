# 📦 StockFlowAPI

A full-stack inventory management system built using FastAPI, PostgreSQL, SQLAlchemy, and a React frontend. It supports full CRUD operations on products and demonstrates backend API development with database integration.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) operations for products  
- RESTful API built using FastAPI  
- PostgreSQL database integration using SQLAlchemy ORM  
- Data validation using Pydantic  
- CORS enabled for frontend integration  
- Auto database initialization with seed data  
- Modular backend structure  
- React frontend for UI interaction  

---

## 🏗️ Tech Stack

Backend: FastAPI, SQLAlchemy, PostgreSQL, Pydantic, Uvicorn  
Frontend: React (Vite/CRA), Axios / Fetch API, HTML, CSS  

---

## 📁 Project Structure

StockFlowAPI/  
├── backend/  
│   ├── main.py  
│   ├── database.py  
│   ├── models.py  
│   ├── database_models.py  
│   ├── .env  
│   └── venv/  
│  
├── frontend/  
│   ├── src/  
│   ├── public/  
│   ├── package.json  
│   └── node_modules/  
│  
├── README.md  

---

## ⚙️ Setup Instructions

### Clone the repository
git clone https://github.com/your-username/StockFlowAPI.git  
cd StockFlowAPI  

---

### Backend Setup
cd backend  
python -m venv venv  
venv\Scripts\activate  

pip install -r requirements.txt  

Create .env file:  
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/yourdbname  

Run backend:  
uvicorn main:app --reload  

Backend URL: http://127.0.0.1:8000  
API Docs: http://127.0.0.1:8000/docs  

---

### Frontend Setup
cd frontend  
npm install  
npm run dev  

Frontend URL: http://localhost:3000  

---

## 🔗 API Endpoints

GET /products → Get all products  
GET /products/{id} → Get product by ID  
POST /products → Add new product  
PUT /products/{id} → Update product  
DELETE /products/{id} → Delete product  

---

## 🧠 Environment Variables

Create a .env file in backend:

DATABASE_URL=postgresql://username:password@localhost:5432/dbname  

---

## ❗ Common Issues

- If dotenv error occurs → pip install python-dotenv  
- If DB fails → check PostgreSQL running + correct password + port  
- If CORS error → ensure allow_origins includes frontend URL  

---

## 📌 Production Improvements

- Add Alembic migrations  
- Move seed data out of main.py  
- Use environment variables everywhere  
- Add authentication  
- Add logging  
- Dockerize application  
- Add pagination for APIs  
- Remove hardcoded credentials  

---

## 👨‍💻 Author

Amaan Shikalgar  

---

## 📜 License

MIT License
