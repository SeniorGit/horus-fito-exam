# Horus Exam Project
Fullstack website untuk management user dengan frontend framework Vue.js + Vite dan backend framwork Flask Python.

## Tech Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript Framework
- **Vite** - Fast Build Tool
- **Vue Router** - Client-side Routing
- **Pinia** - State Management
- **Axios** - HTTP Client

### Backend
- **Flask** - Python Web Framework
- **PostgreSQL** - Database
- **JWT** - Authentication
- **Flask-CORS** - Cross-Origin Resource Sharing
- **psycopg2** - PostgreSQL Adapter

## Quick Start 

### Backend Setup

1. **Pergi ke backend directory**
```bash 
cd backend
```

2. **Buat virtual Eviroment**
```bash
python -m venv venv
source venv/bin/activate  
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Configuration**
```bash
DB_HOST=localhost
DB_USER=postgres
DB_PASSWORD=123
DB_NAME=horus_fito_db
DB_PORT=5432

JWT_SECRET_KEY=8f3a9b7c5d2e1f4a6b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0
SECRET_KEY=123f3asd3429b7c5d2e1ewfsf4a6b8c9d0e1f2a3b4c5d6e7f8a3432423b0c1d2e3f
CORS_ORIGINS=http://localhost:5173
```

5. **Jalankan database migrations**
```bash
flask db upgrade
```

6. **Jalankan Backend**
```bash
python run.py
```

### Frontend Setup

1. **Pergi ke Frontend directory**
```bash 
cd frontend
```

2. **Install Dependencies**
```bash
npm install
```

3. **Start development**
```bash
npm run dev
```


