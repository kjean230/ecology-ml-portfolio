# crud.py 
# CRUD operations for user management and preset handling
from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password, verify_password

# creates a method that gets a user by email
# returns None if not found
def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()

# creates a new user with hashed password
# returns the created user
def create_user(db: Session, user_in: schemas.UserCreate) -> models.User:
    hashed = hash_password(user_in.password)
    user = models.User(email=user_in.email, password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# authenticates a user by email and password
# returns the user if authentication is successful, else None
def authenticate_user(db: Session, email: str, password: str) -> models.User | None:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user