# trees_1995_import.py
# ETL script to import 1995 tree census data into the database
import re
from pathlib import Path

import numpy as np
import pandas as pd
from ..database import SessionLocal
from ..models_trees import Tree

CSV_FILE_PATH = Path(__file__).resolve().parent / "data" / "1995_Street_Tree_Census.csv"
YEAR = 1995
BATCH_SIZE = 5000

def normalize_headers(cols):
    """
    Normalize column headers within the DataFrame.
    """
    return [c.strip().lower().replace(" ", "_") for c in cols]

def to_int(s):
    """
    Convert a string to an integer, removing commas and spaces.
    Returns None if conversion is not possible.
    """
    if s is None:
        return None
    t = re.sub(r"[,\s]", "", str(s))
    return int(t) if t != "" and re.fullmatch(r"-?\d+", t) else None

def to_int_bounds(s, low=0, high=100):
    """
    Convert a string to an integer within specified bounds.
    Returns None if conversion is not possible or out of bounds.
    """
    v = to_int(s)
    if v is None:
        return None
    return v if (low <= v <= high) else None

def to_dec(s):
    ...