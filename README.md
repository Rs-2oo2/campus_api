# Campus Assignment API

A Django REST API for managing student registrations and assignments.
Students can register, log in, and manage their assignments.

---

# Tech Stack

* Python 3.11
* Django
* Django REST Framework
* PostgreSQL
* Postman (API Testing)

---
#Project Structure


campus-assignment-api/
│
├── config/
│   ├── assignments/
│   ├── accounts/
│   └── config/
│   ├── Campus_Project.postman_collection.json/
│   ├── schema/
│   └── manage.py/
│   └── requirements.txt/
│
├── venv/
├── .gitignore/
└── README.md
# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Rs-2oo2/campus_api.git
cd campus_api
```

## 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
 cd config
pip install -r requirements.txt
```

## 4. Setup PostgreSQL Database

Create a database in PostgreSQL:

```
Database Name: campus_db
Username: postgres
Password: your_password
```

## 5. Configure Environment

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'campus_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


## 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Create Superuser

```bash
python manage.py createsuperuser
```

Example:

```
username: admin
email: admin@gmail.com
password: admin123

```

---

## 8. Run Server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

# Database Schema

## Student Table

```
Student
------
id
username
email
password
department
year
```

## Assignment Table

```
Assignment
----------
id
title
description
status
student_id
created_at
```

---

# API Endpoints

## Base URL

```
http://127.0.0.1:8000/api/
```

---

## 1. Register Student

POST `/api/register/`

### Request

```json
{
  "name": "Rojan Sebastian",
  "email": "rojan@gmail.com",
  "password": "123456",
  "department": "Computer Science",
  "year": 3
}
```

### Response

```json
{
  "id": 1,
  "name": "Rojan Sebastian",
  "email": "rojan@gmail.com",
  "department": "Computer Science",
  "year": 3
}
```

---

## 2. Login

POST `/api/login/`

### Request

```json
{
  "username": "RojanSebastian",
  "password": "123456"
}
```

### Response

```json
{
  "token": "your_token_here"
}
```

---

## 3. Create Assignment

POST `/api/assignments/`

Headers:

```
Authorization: Token your_token
```

### Request

```json
{
  "title": "Math Assignment",
  "description": "Complete exercises 1-5",
  "status": "pending"
}
```

### Response

```json
{
  "id": 1,
  "title": "Math Assignment",
  "description": "Complete exercises 1-5",
  "status": "pending"
}
```

---

## 4. Get All Assignments

GET `/api/assignments/`

### Response

```json
[
  {
    "id": 1,
    "title": "Math Assignment",
    "description": "Complete exercises 1-5",
    "status": "pending"
  }
]
```

---

## 5. Get Single Assignment

GET `/api/assignments/{id}/`

---

## 6. Update Assignment

PUT `/api/assignments/{id}/`

---

## 7. Change Assignment Status

PATCH `/api/assignments/{id}/`

### Request

```json
{
  "status": "completed"
}
```

---

## 8. Delete Assignment

DELETE `/api/assignments/{id}/`

---

# Postman Collection

Postman collection is included:

```
Campus_Project.postman_collection.json
```

Import into Postman:

1. Open Postman
2. Click Import
3. Select the JSON file -(Campus_Project.postman_collection.json)



# Sample Workflow

1. Register student
2. Login
3. Copy token
4. Create assignment
5. Update status
6. View assignments

---



# Author

Rojan Sebastian
