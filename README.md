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
  <img src="https://via.placeholder.com/900x450.png?text=Add+Your+Frontend+Screenshot+Here" width="80%"/>
</p>

## ⚡ Features

- Full CRUD operations on products
- FastAPI REST API backend
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic validation
- React frontend integration
- CORS configured for frontend
- Auto database seeding

## 🧠 Tech Stack

Backend: FastAPI, SQLAlchemy, PostgreSQL, Pydantic, Uvicorn  
Frontend: React (Vite), Axios, HTML, CSS  

## 📁 Project Structure

StockFlowAPI  
├── backend  
│   ├── main.py  
│   ├── database.py  
│   ├── models.py  
│   ├── database_models.py  
│   ├── .env (ignored)  
│  
├── frontend  
│   ├── src  
│   ├── public  
│   ├── package.json  
│  
└── README.md  

## 🚀 API Endpoints

GET /products → Get all products  
GET /products/{id} → Get product by id  
POST /products → Add product  
PUT /products/{id} → Update product  
DELETE /products/{id} → Delete product  

## ⚙️ Setup Instructions

Clone repo  
git clone https://github.com/your-username/StockFlowAPI.git  
cd StockFlowAPI  

Backend setup  
cd backend  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  

Create .env  
DATABASE_URL=postgresql://postgres:password@localhost:5432/stockflow  

Run backend  
uvicorn main:app --reload  

Backend runs at http://127.0.0.1:8000  
Docs at http://127.0.0.1:8000/docs  

Frontend setup  
cd frontend  
npm install  
npm run dev  

Frontend runs at http://localhost:3000  

## 🧠 Learnings

- FastAPI backend architecture
- PostgreSQL + SQLAlchemy integration
- Full CRUD API design
- Frontend-backend integration
- Debugging deployment issues

## 👨‍💻 Author

Amaan Shikalgar — Full Stack Developer

## ⭐ Support

If you like this project, star the repository ⭐
