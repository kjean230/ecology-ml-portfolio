from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, init_db  # NOTE: relative import

# makes a FastAPI instance
app = FastAPI(
    title="Ecology ML Portfolio API",
    version="0.1.0",
)

@app.on_event("startup")
def on_startup():
    init_db()

# this function provides a database session for each request
# a way to speak to the database from the backend
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}