# backend/app/models_trees.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Tree(Base):
    __tablename__ = "trees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # ID from the census (e.g., recordid)
    tree_id = Column(Integer, index=True)

    # Year of census (1995, 2005, 2015)
    year = Column(Integer, index=True)

    # Basic attributes for S1
    borough = Column(String(50), index=True)
    species = Column(String(255), index=True)

    # Health labels + numeric score
    health = Column(String(50), index=True)        # "Good", "Fair", "Poor"
    health_score = Column(Integer, index=True)     # 2 / 1 / 0

    # Location and size
    latitude = Column(Float)
    longitude = Column(Float)
    dbh = Column(Float)  # diameter at breast height