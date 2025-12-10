# models_trees.py
# creates a Tree model for storing hierarchical tree data
# implementation will be added in the future

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Tree(Base):
    __tablename__ = "trees"

    # Defining columns for the Tree model
    # these are columns that will be prepared for the values from CSV files
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tree_id = Column(Integer, index=True)
    year = Column(Integer, index=True)
    borough = Column(String(100), index=True)
    species = Column(String(255), index=True)

    # Additional attributes for tree data
    # the health score column will be used for ML predictions
    health = Column(String(50), index=True)
    health_score = Column(Integer, index=True)

    longitude = Column(Float, index=True)
    latitude = Column(Float, index=True)
    dbh = Column(Integer, index=True)  # Diameter at Breast Height