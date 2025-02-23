# FastAPI Starter Template 🚀  

A ready-to-use **FastAPI starter project** with PostgreSQL integration, database migrations, and essential configurations to jumpstart your next web application.  
---

## ✨ Features  
- **PostgreSQL Database Integration** with SQLAlchemy.  
- **Automatic Superuser Creation** on setup.  
- **Database Migrations** using Alembic.  
- **CORS Middleware** for handling cross-origin requests.  
- Predefined **Users** and **Items** models and endpoints.  
- Interactive **API Documentation** at `/docs`.  

---

## 📋 Requirements  
- **Python 3.9+**  
- **PostgreSQL**  

---

## 🚀 Installation  

Follow these steps to set up and run the project:  

### 1. Clone the Repository  
```bash
git clone https://github.com/ftoucch/Fast-API-Starter-Template.git
cd Fast-API-Starter-Template
```

### 2. Create a Virtual Environment  
```bash
python -m venv venv  
source venv/bin/activate 
```
# For Windows: 
```bash
venv\Scripts\activate
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Set Up `.env`  
Rename `env-example` to `.env` and update it with your database credentials and other configurations.  

### 5. Alembic Migrations  
Run the following commands to set up and apply the database migrations: 

```bash
alembic upgrade head  
```

### 6. Start the Application  
Run the FastAPI app with:  
```bash
uvicorn app.main:app --reload
```


## 🛠 Endpoints  

### Users  
- **GET** `/api/v1/users`  

### Items  
- **GET** `/api/v1/items`  

---

## 📚 API Documentation  
Interactive API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).  

---

## 💡 Why Use This Starter Template?  
This starter template is perfect for:  
- Developers looking for a quick setup to build a **FastAPI** application.  
- Seamless integration with **PostgreSQL** and **SQLAlchemy**.  
- Easy database schema migrations with **Alembic**.  
- A clean and modular project structure for efficient API development.  

---

Happy coding! 🎉  
