# 🚀 Medical Backend API (FastAPI)

A high-performance backend API built using **FastAPI**, designed with a clean architecture and modern async practices. This project demonstrates real-world backend development skills including authentication, file uploads, and database management.

---

## 🔥 Features

* 🔐 User Authentication (JWT-based)
* 📦 Product / Order Management APIs
* ☁️ File Upload Integration (Cloudinary)
* ⚡ Fully Asynchronous APIs using `async/await`
* 🗄️ PostgreSQL Database Integration
* 🧠 Clean Architecture (Routes → Services → Models)

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy (Async)
* **Authentication:** JWT
* **File Storage:** Cloudinary
* **Validation:** Pydantic
* **Server:** Uvicorn

---

## ⚡ Async Architecture (Important)

This project is built using **asynchronous programming**:

* Uses `async def` endpoints
* Database operations handled with `AsyncSession`
* Non-blocking request handling for better performance

> This ensures high scalability and faster response times compared to traditional synchronous APIs.

---

## 📁 Project Structure

```
app/
 ├── routes/        # API endpoints
 ├── services/      # Business logic
 ├── models/        # Database models
 ├── schemas/       # Pydantic schemas
 ├── utils/         # Helper functions (auth, db, etc.)
 └── main.py        # Entry point
```

---

## 📦 API Capabilities

* Create, fetch, and delete records
* Upload and store files via Cloudinary
* Secure user login and token generation
* Efficient database querying using SQLAlchemy

---

## ▶️ Run Locally

```bash
git clone <your-repo-link>
cd project-folder

pip install -r requirements.txt

uvicorn main:app --reload
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
DATABASE_URL=your_database_url
CLOUD_NAME=your_cloud_name
API_KEY=your_api_key
API_SECRET=your_api_secret
SECRET_KEY=your_jwt_secret
```

---

## 🎯 Why This Project?

This project showcases:

* Real-world backend development practices
* Understanding of async programming in Python
* Integration with external services (Cloudinary)
* Clean and scalable API design

---

## 🚀 Future Improvements

* Redis caching
* Background task handling (Celery)
* Email notifications system
* WebSocket support for real-time features

---

## 👨‍💻 Author

Built with focus on becoming a **production-ready backend developer**.

---
