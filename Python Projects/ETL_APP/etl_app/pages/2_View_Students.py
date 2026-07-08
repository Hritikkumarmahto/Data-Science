"""
pages/2_View_Students.py
Full CRUD view for students:
  - Read:   list of all students pulled from MySQL
  - Update: "⋮" menu -> Edit -> opens a dialog with a pre-filled form
  - Delete: "⋮" menu -> Delete -> confirm -> removes from MySQL

Also includes a tab showing the raw JSON staging file for transparency.
"""

import streamlit as st
import pandas as pd
from database.models import (
    get_students,
    get_student_by_id,
    update_student,
    delete_student,
    count_students,
)
from database.db_connector import db
from services import json_store

st.set_page_config(page_title="View Students", page_icon="🎓", layout="wide")
st.title("🎓 Students")

ok, msg = db.test_connection()
if not ok:
    st.error(f"Database not reachable: {msg}")
    st.stop()


# ---------------------------------------------------------------------
# Edit dialog (Update)
# ---------------------------------------------------------------------
@st.dialog("Edit Student")
def edit_student_dialog(student):
    st.write(f"Editing record #{student['id']}")

    student_id = st.text_input("Student ID / Roll No", value=student.get("student_id") or "")
    name = st.text_input("Full Name *", value=student.get("name") or "")
    email = st.text_input("Email", value=student.get("email") or "")
    phone = st.text_input("Phone", value=student.get("phone") or "")
    course = st.text_input("Course", value=student.get("course") or "")
    city = st.text_input("City", value=student.get("city") or "")

    dob_value = student.get("dob")
    dob = st.date_input("Date of Birth", value=dob_value)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save changes", type="primary", use_container_width=True):
            if not name.strip():
                st.error("Full Name is required.")
            else:
                dob_str = dob.isoformat() if dob else None
                update_student(
                    student["id"],
                    student_id.strip() or None,
                    name.strip(),
                    email.strip() or None,
                    phone.strip() or None,
                    course.strip() or None,
                    city.strip() or None,
                    dob_str,
                )
                st.success("Student updated.")
                st.rerun()
    with col2:
        if st.button("Cancel", use_container_width=True):
            st.rerun()


# ---------------------------------------------------------------------
# Delete confirmation dialog
# ---------------------------------------------------------------------
@st.dialog("Delete Student")
def delete_student_dialog(student):
    st.warning(f"Are you sure you want to delete **{student['name']}** (record #{student['id']})? "
               f"This cannot be undone.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, delete", type="primary", use_container_width=True):
            delete_student(student["id"])
            st.success("Student deleted.")
            st.rerun()
    with col2:
        if st.button("Cancel", use_container_width=True):
            st.rerun()


tab1, tab2 = st.tabs(["In Database (MySQL)", "JSON staging file"])

with tab1:
    total = count_students()
    st.metric("Total students in database", total)

    students = get_students(limit=500)

    if not students:
        st.info("No students in the database yet. Add one on the 'Add Student' page.")
    else:
        search = st.text_input("Search by name, email, or student ID", "")
        if search.strip():
            s = search.strip().lower()
            students = [
                r for r in students
                if s in (r.get("name") or "").lower()
                or s in (r.get("email") or "").lower()
                or s in (str(r.get("student_id") or "")).lower()
            ]

        st.divider()

        # Header row
        header_cols = st.columns([1, 2, 2, 2, 2, 2, 1])
        for col, label in zip(header_cols, ["ID", "Name", "Email", "Phone", "Course", "City", ""]):
            col.markdown(f"**{label}**")

        # One row per student, with a "⋮" popover menu for Edit/Delete
        for student in students:
            c1, c2, c3, c4, c5, c6, c7 = st.columns([1, 2, 2, 2, 2, 2, 1])
            c1.write(student["id"])
            c2.write(student["name"] or "-")
            c3.write(student["email"] or "-")
            c4.write(student["phone"] or "-")
            c5.write(student["course"] or "-")
            c6.write(student["city"] or "-")

            with c7.popover("⋮"):
                if st.button("✏️ Edit", key=f"edit_{student['id']}", use_container_width=True):
                    edit_student_dialog(student)
                if st.button("🗑️ Delete", key=f"delete_{student['id']}", use_container_width=True):
                    delete_student_dialog(student)

        st.divider()
        df = pd.DataFrame(students)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download as CSV", csv, "students.csv", "text/csv")

with tab2:
    st.write("This is the raw content of `data/students.json` — the intermediate "
             "file every form submission passes through before reaching MySQL.")
    all_records = json_store.read_all()
    pending = [r for r in all_records if not r.get("loaded", False)]

    if pending:
        st.warning(f"{len(pending)} record(s) in the JSON file are not yet loaded into MySQL.")
    else:
        st.success("All records in the JSON file have been loaded into MySQL.")

    st.json(all_records)
