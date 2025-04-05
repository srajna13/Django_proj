
# Pet Adoption System

A **Django REST API** for a pet adoption system with role-based authentication (admin & users), allowing users to adopt and return pets.

## **Features**
- User authentication with JWT (Signup, Login, Logout, Refresh)  
- Role-based access control (Admin & User)  
- CRUD operations for pets (Admin only)  
- Adoption & return of pets (Users only)  
- MySQL database integration  
- Automated testing with Pytest  
- Code linting with Pylint  
- Test coverage analysis with Pytest-Cov  

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

The API will be available at http://127.0.0.1:8000

To access admin panel, visit : http://127.0.0.1:8000/admin

---

## **API Endpoints**

### **Authentication Endpoints**
#### **Sign Up (Direct URL Access)**
Open in browser:
```
http://127.0.0.1:8000/api/signup/
```
Use POST method with:
```json
{
  "username": "testuser",
  "password": "testpass123"
}
```
#### **Login (Direct URL Access)**
Open in browser:
```
http://127.0.0.1:8000/api/login/
```
Use POST method with:
```json
{
  "username": "testuser",
  "password": "testpass123"
}
```
**Response:**
```json
{
  "access": "<ACCESS_TOKEN>",
  "refresh": "<REFRESH_TOKEN>"
}
```
#### **Logout**
```
curl -X POST http://127.0.0.1:8000/api/auth/logout/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```
### **User Endpoints** *(JWT Authentication Required)*

#### **View All Adoptable Pets**
```
curl -X GET http://127.0.0.1:8000/api/pets/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

#### **Adopt a Pet**
```
curl -X POST http://127.0.0.1:8000/api/pets/<PET_ID>/adopt/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```
---

### **Admin Endpoints** *(Admin + JWT Authentication Required)*
#### **Add a Pet**
Open in browser
```
http://localhost:8000/admin/adoption/pet/add/

```
#### **Update Pet**
```
http://localhost:8000/admin/adoption/pet/<pet_id>/change/
```
#### **Delete a pet**
```
http://localhost:8000/admin/adoption/pet/<pet_id>/delete/
```
#### **View all pets**
```
http://localhost:8000/admin/adoption/pet/
```
#### **View all adoptions**
```
http://localhost:8000/admin/adoption/adoption/
```

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

