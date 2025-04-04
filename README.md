
# Pet Adoption System

A **Django REST API** for a pet adoption system with role-based authentication (admin & users), allowing users to adopt and return pets.

## **Features**
✅ User authentication with JWT (Signup, Login, Logout, Refresh)  
✅ Role-based access control (Admin & User)  
✅ CRUD operations for pets (Admin only)  
✅ Adoption & return of pets (Users only)  
✅ MySQL database integration  
✅ Automated testing with Pytest  
✅ Code linting with Pylint  
✅ Test coverage analysis with Pytest-Cov  

---

## **Installation**
### **1. Clone the Repository**
```sh
git clone <repository url>
cd pet_adoption_system
```

### **2. Create and Activate Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Configure MySQL Database**
Update `.env` with your **MySQL credentials**:
```ini
DB_NAME=your_database_name
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your_secret_key
```

### **5. Apply Migrations**
```sh
python manage.py migrate
python manage.py createsuperuser  # Create admin user
```

### **6. Run the Development Server**
```sh
python manage.py runserver
```
Access API docs at: `http://127.0.0.1:8000/swagger/`

---

## **API Endpoints**
### **Authentication**
- `POST /auth/signup/` → Register user
- `POST /auth/login/` → Get access & refresh tokens
- `POST /auth/logout/` → Logout user
- `POST /auth/refresh/` → Refresh token
- `GET /auth/me/` → Get user details
- `PUT /auth/me/` → Update user profile

### **Admin (Protected Routes)**
- `POST /admin/pets/` → Add a pet
- `PUT /admin/pets/{id}/` → Update pet details
- `DELETE /admin/pets/{id}/` → Remove a pet
- `GET /admin/pets/` → View all pets
- `GET /admin/adoptions/` → View all adoptions

### **Users**
- `GET /pets/` → View adoptable pets
- `POST /pets/{id}/adopt/` → Adopt a pet
- `POST /pets/{id}/return/` → Return a pet
- `GET /pets/history/` → View adoption history

---

## **Code Quality & Linting**
### **Run Pylint to Check Code Quality**
```sh
pylint adoption
```

---

## **Testing & Coverage**
### **Run Tests with Pytest**
```sh
pytest
```
### **Check Test Coverage**
```sh
pytest --cov=adoption --cov-report=term-missing
```
### **Generate HTML Coverage Report**
```sh
pytest --cov=adoption --cov-report=html
open htmlcov/index.html  # macOS/Linux
start htmlcov/index.html  # Windows
```
### **Enforce Minimum Coverage (Fail if <80%)**
```sh
pytest --cov=adoption --cov-fail-under=80
```

---

## **Contributing**
1. **Fork** the repo
2. **Create** a new branch (`git checkout -b feature-branch`)
3. **Commit** your changes (`git commit -m "Add feature"`)
4. **Push** to your branch (`git push origin feature-branch`)
5. **Submit** a pull request

---

## **License**
This project is licensed under the **MIT License**.

---

### 🚀 **Happy Coding!**

