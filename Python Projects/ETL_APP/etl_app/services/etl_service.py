"""
services/etl_service.py
Orchestrates the pipeline:
  EXTRACT  -> services.json_store (reads unloaded records from students.json)
  TRANSFORM-> services.transformer
  LOAD     -> database.models (inserts into MySQL 'students' table)

Every load attempt is recorded in the etl_log table.
"""

from services import json_store, transformer
from database import models

JSON_FILE_LABEL = "data/students.json"


def _safe_log(source_file, rows_loaded, status, message=""):
    """
    Writes to etl_log but never lets a logging failure crash the caller.
    If etl_log itself doesn't exist yet, this just prints instead of raising.
    """
    try:
        models.log_etl_run(source_file, rows_loaded, status, message)
    except Exception as log_err:
        print(f"[etl_log write failed, ignoring] {log_err}")


def load_pending_students_to_db():
    """
    Reads every student record in students.json not yet marked 'loaded',
    inserts them into MySQL, and marks them loaded on success.
    Returns (success: bool, message: str, rows_loaded: int)
    """
    # Make sure the tables exist before doing anything else. This is a
    # cheap CREATE TABLE IF NOT EXISTS, safe to run on every call.
    try:
        models.init_db()
    except Exception as e:
        return False, f"Could not verify/create tables: {e}", 0

    pending = json_store.read_unloaded()

    if not pending:
        return True, "No new records to load — everything is already in the database.", 0

    try:
        rows = transformer.transform_students(pending)
        affected = models.bulk_insert_students(rows)
        json_store.mark_all_loaded()
        _safe_log(JSON_FILE_LABEL, affected, "SUCCESS")
        return True, f"Loaded {affected} student record(s) into the database.", affected
    except Exception as e:
        _safe_log(JSON_FILE_LABEL, 0, "FAILED", str(e))
        return False, f"Failed to load records into the database: {e}", 0


def submit_student_form(student_id, name, email, phone, course, city, dob):
    """
    Full pipeline for one form submission:
      1. Append to data/students.json (intermediate JSON store)
      2. Immediately run the ETL load step into MySQL
    Returns (success: bool, message: str)
    """
    record = {
        "student_id": student_id,
        "name": name,
        "email": email,
        "phone": phone,
        "course": course,
        "city": city,
        "dob": dob,
    }
    json_store.append_student(record)
    ok, message, _ = load_pending_students_to_db()
    return ok, message
