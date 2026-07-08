"""
database/models.py
Defines the tables used by this ETL app and helpers to create/use them.

1. students  -> final structured table where student data lands.
2. etl_log   -> tracks each JSON -> DB load (file, row count, status).
"""

from database.db_connector import db

CREATE_STUDENTS_TABLE = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NULL,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NULL,
    phone VARCHAR(20) NULL,
    course VARCHAR(100) NULL,
    city VARCHAR(100) NULL,
    dob DATE NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

CREATE_ETL_LOG_TABLE = """
CREATE TABLE IF NOT EXISTS etl_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source_file VARCHAR(255) NOT NULL,
    rows_loaded INT NOT NULL DEFAULT 0,
    status VARCHAR(50) NOT NULL,
    message TEXT NULL,
    run_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""


def init_db():
    """Create all required tables if they do not exist."""
    db.execute(CREATE_STUDENTS_TABLE)
    db.execute(CREATE_ETL_LOG_TABLE)


def insert_student(student_id, name, email, phone, course, city, dob):
    query = """
        INSERT INTO students (student_id, name, email, phone, course, city, dob)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    return db.execute(query, (student_id, name, email, phone, course, city, dob))


def bulk_insert_students(rows):
    """
    rows: list of tuples (student_id, name, email, phone, course, city, dob)
    """
    query = """
        INSERT INTO students (student_id, name, email, phone, course, city, dob)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    return db.executemany(query, rows)


def get_students(limit=200):
    query = "SELECT * FROM students ORDER BY created_at DESC LIMIT %s"
    return db.fetch_all(query, (limit,))


def get_student_by_id(record_id):
    query = "SELECT * FROM students WHERE id = %s"
    return db.fetch_one(query, (record_id,))


def update_student(record_id, student_id, name, email, phone, course, city, dob):
    query = """
        UPDATE students
        SET student_id = %s, name = %s, email = %s, phone = %s,
            course = %s, city = %s, dob = %s
        WHERE id = %s
    """
    db.execute(query, (student_id, name, email, phone, course, city, dob, record_id))


def delete_student(record_id):
    db.execute("DELETE FROM students WHERE id = %s", (record_id,))


def count_students():
    row = db.fetch_one("SELECT COUNT(*) AS total FROM students")
    return row["total"] if row else 0


def log_etl_run(source_file, rows_loaded, status, message=""):
    query = """
        INSERT INTO etl_log (source_file, rows_loaded, status, message)
        VALUES (%s, %s, %s, %s)
    """
    return db.execute(query, (source_file, rows_loaded, status, message))


def get_recent_logs(limit=20):
    query = "SELECT * FROM etl_log ORDER BY run_at DESC LIMIT %s"
    return db.fetch_all(query, (limit,))
