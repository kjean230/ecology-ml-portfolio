from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# Define User model
# this model represents the users in the system
# contains their email, password hash, and creation timestamp
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    presets = relationship("Preset", back_populates="user", cascade="all, delete-orphan")

# Define Preset model
# this model represents user-defined presets for data filtering
# includes study identifier, name, filter settings in JSON, and creation timestamp
class Preset(Base):
    __tablename__ = "presets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    study_id = Column(String(50), nullable=False)  # e.g., "S1", "S2"
    name = Column(String(255), nullable=False)     # user-friendly label
    filters_json = Column(Text, nullable=False)    # JSON string of filters
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="presets")