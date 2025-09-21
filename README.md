# FlaskUserRegistrationSystem

## Features
- User registration and login with JWT authentication
- Profile retrieval and update
- Password change endpoint
- Account deletion
- MySQL database integration
- Dockerized for easy deployment

## Tech Stack
- Python 3.11
- Flask
- MySQL
- Flask-JWT-Extended
- Flask-Bcrypt
- SQLAlchemy
- Docker & Docker Compose

## Installation
### 1. Clone the repository

```bash
git clone https://github.com/Sanjaa46/FlaskUserRegistrationSystem
cd UserRegistrationSystem
```
### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```
### 3. Set up MySQL database

```sql
CREATE DATABASE user_db;
```
### 4.Update config.py with your database credentials

## Running the App
### Without Docker
```bash
python app.py
```
App runs on http://localhost:5000.

### With Docker
```bash
docker-compose up --build
```
- Flask app → port 5000
- MySQL → port 3306/3307

## API Endpoints
- POST /register → Register new user
- POST /login → Login and get JWT
- GET /profile → Get user profile (JWT required)
- PUT /profile/password → Change password (JWT required)
- DELETE /profile → Delete account (JWT required)



