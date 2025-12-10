# trees_1995_import.py
# Script to import 1995 tree census data into the database

import re
from pathlib import Path

import numpy as np
import pandas as pd
from ..database import SessionLocal
from ..models_trees import Tree

# creates a path to the csv file
# marks the year at 1995 and batch size at 5000
CSV_TREE_PATH = Path(__file__).resolve().parent.parent / "data" / "1995_Street_Tree_Census.csv"
YEAR = 1995
BATCH_SIZE = 5000

# --- HELPER FUNCTIONS --- #

# function to normalize columns within the csv file
def normalize_headers(cols):
    # implementation to normalize all headers to snake_case
    return [c.strip().lower().replace(" ", "_") for c in cols]

# function to convert strings to integers, handling commas and spaces
def to_int(s): 
    if s is None:
        return None
    t = re.sub(r"[,\s]", "", str(s))
    return int(t) if t != "" and re.fullmatch(r"-?\d+", t) else None