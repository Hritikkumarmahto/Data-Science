"""
services/transformer.py
TRANSFORM step. Takes raw student dicts (as read from data/students.json)
and turns them into tuples ready for database.models.bulk_insert_students.
"""


def clean_value(value):
    """Turn empty strings into None so blank form fields become NULL in DB."""
    if value is None:
        return None
    if isinstance(value, str) and value.strip() == "":
        return None
    return value


def transform_students(raw_records):
    """
    Input:  list of dicts like
            {"student_id": "S1", "name": "...", "email": "...",
             "phone": "...", "course": "...", "city": "...", "dob": "2005-04-12"}
    Output: list of tuples matching models.bulk_insert_students order:
            (student_id, name, email, phone, course, city, dob)
    """
    rows = []
    for rec in raw_records:
        rows.append((
            clean_value(rec.get("student_id")),
            clean_value(rec.get("name")),
            clean_value(rec.get("email")),
            clean_value(rec.get("phone")),
            clean_value(rec.get("course")),
            clean_value(rec.get("city")),
            clean_value(rec.get("dob")),
        ))
    return rows
