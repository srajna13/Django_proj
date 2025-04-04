# Pet Adoption System

## 📌 Overview
The **Pet Adoption System** is a Django-based REST API that allows users to adopt and return pets. It includes authentication, role-based access control (admin & users), and MySQL integration.

## 🚀 Features
- User authentication (Signup, Login, Logout, JWT Refresh)
- Admin can add, update, and delete pet records
- Users can view and adopt available pets
- Adoption history tracking
- Role-based access control
- API testing using Pytest

---

## 📂 Project Structure
```
pet_adoption_system/
│── adoption/          # Main app (models, views, serializers, tests)
│── pet_adoption_system/  # Django settings & URLs
│── requirements.txt   # Dependencies
│── pytest.ini         # Pytest config
│── manage.py          # Django entry point
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/pet_adoption_system.git
cd pet_adoption_system
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file and add the following:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=mysql://username:password@localhost:3306/pet_adoption_db
```

### 5️⃣ Apply Database Migrations
```bash
python manage.py migrate
```

### 6️⃣ Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server
```bash
python manage.py runserver
```
The API will be available at: `http://127.0.0.1:8000/`

---

## 🔑 Authentication Endpoints
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| POST   | `/auth/signup/`  | Register a new user |
| POST   | `/auth/login/`   | Get JWT access & refresh tokens |
| POST   | `/auth/logout/`  | Logout user |
| POST   | `/auth/refresh/` | Refresh JWT token |

## 🐶 Pet Endpoints
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/pets/`                | View all available pets |
| POST   | `/pets/{id}/adopt/`     | Adopt a pet |
| POST   | `/pets/{id}/return/`    | Return a pet |
| GET    | `/pets/history/`        | View adoption history |

## 🛠️ Admin Endpoints
| Method | Endpoint            | Description |
|--------|---------------------|-------------|
| POST   | `/admin/pets/`      | Add a pet |
| PUT    | `/admin/pets/{id}/` | Update pet details |
| DELETE | `/admin/pets/{id}/` | Remove a pet |
| GET    | `/admin/adoptions/` | View all adoption records |

---

## ✅ Running Tests
Run **Pytest** to ensure everything works correctly:
```bash
pytest
```

---

## 💡 Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m "Added new feature"`
4. Push to the branch: `git push origin feature-branch`
5. Open a Pull Request

---
