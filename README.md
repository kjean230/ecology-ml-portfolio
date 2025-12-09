# Ecology ML Portfolio

Backend groundwork for forecasting urban tree health trends. A FastAPI service is wired up with database models, auth utilities, and CRUD helpers so user-facing routes and visualizations can be added next.

## What’s implemented
- FastAPI app with a `/health` endpoint and automatic DB table creation on startup.
- MySQL connection via SQLAlchemy; settings loaded from a `.env` file.
- ORM models for `User` (email, password hash, timestamps) and `Preset` (per-user saved filter configurations).
- Auth helpers for bcrypt password hashing and JWT creation/verification.
- CRUD helpers for creating users, fetching by email, and authenticating with hashed passwords.

## Project layout
- `backend/app/main.py` — FastAPI entrypoint, startup DB init, health check.
- `backend/app/database.py` — SQLAlchemy engine/session setup using MySQL env vars.
- `backend/app/models.py` — `User` and `Preset` ORM models.
- `backend/app/schemas.py` — Pydantic schemas for users and presets.
- `backend/app/auth.py` — Password hashing and JWT encode/decode utilities.
- `backend/app/crud.py` — User creation, lookup, and authentication helpers.

## Setup
1) Create a Python env and install backend deps:
```bash
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv passlib[bcrypt] python-jose
```
2) Add a `.env` in `backend/app` (or repo root) with:
```
MYSQL_USER=...
MYSQL_PASSWORD=...
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=...
JWT_SECRET_KEY=change_me_in_prod
```

## Running the API
```bash
uvicorn backend.app.main:app --reload
```
The service will create tables on startup and expose `http://localhost:8000/health`.

## Next steps
- Add FastAPI routes for user signup/login and preset management using the existing CRUD/auth helpers.
- Build the frontend data visualization dashboard and connect it to the API.
