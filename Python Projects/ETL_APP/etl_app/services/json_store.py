"""
services/json_store.py
This is the "JSON is intermediate" layer.

Flow:
  Streamlit form  --(1) append -->  data/students.json  --(2) ETL load--> MySQL

Every student submitted through the form is first appended to
data/students.json (a JSON array on disk). The ETL step then reads
that file, inserts the records into MySQL, and marks them as loaded
so they aren't inserted twice.
"""

import json
import os
from config.config import config

STUDENTS_JSON_FILE = os.path.join(config.DATA_FOLDER, "students.json")


def _ensure_file():
    os.makedirs(config.DATA_FOLDER, exist_ok=True)
    if not os.path.exists(STUDENTS_JSON_FILE):
        with open(STUDENTS_JSON_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)


def append_student(record: dict):
    """
    Append one student record (as a dict) to data/students.json.
    Adds a 'loaded' flag (False) so the ETL step knows it's new.
    """
    _ensure_file()
    with open(STUDENTS_JSON_FILE, "r", encoding="utf-8") as f:
        records = json.load(f)

    record = dict(record)  # copy
    record["loaded"] = False
    records.append(record)

    with open(STUDENTS_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, default=str)

    return record


def read_all():
    """Return every record currently in data/students.json."""
    _ensure_file()
    with open(STUDENTS_JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def read_unloaded():
    """Return only the records not yet loaded into MySQL."""
    return [r for r in read_all() if not r.get("loaded", False)]


def mark_all_loaded():
    """Flip every record's 'loaded' flag to True after a successful DB load."""
    _ensure_file()
    with open(STUDENTS_JSON_FILE, "r", encoding="utf-8") as f:
        records = json.load(f)

    for r in records:
        r["loaded"] = True

    with open(STUDENTS_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, default=str)
