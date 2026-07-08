"""
pages/1_Add_Student.py
Streamlit page: a form to enter one student's data.

On submit:
  1. The data is appended to data/students.json (intermediate JSON file).
  2. The ETL step immediately runs, loading any pending JSON records
     into the MySQL 'students' table.
"""

import datetime
import streamlit as st
from services import etl_service

st.set_page_config(page_title="Add Student", page_icon="📝", layout="centered")
st.title("📝 Add Student")
st.caption("Data is first written to data/students.json, then loaded into MySQL.")

with st.form("student_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        student_id = st.text_input("Student ID / Roll No")
        name = st.text_input("Full Name *")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
    with col2:
        course = st.text_input("Course")
        city = st.text_input("City")
        dob = st.date_input(
            "Date of Birth",
            value=None,
            min_value=datetime.date(1990, 1, 1),
            max_value=datetime.date.today(),
        )

    submitted = st.form_submit_button("Save Student", type="primary")

    if submitted:
        if not name.strip():
            st.error("Full Name is required.")
        else:
            dob_str = dob.isoformat() if dob else None
            with st.spinner("Saving to students.json and loading into MySQL..."):
                ok, message = etl_service.submit_student_form(
                    student_id=student_id.strip(),
                    name=name.strip(),
                    email=email.strip(),
                    phone=phone.strip(),
                    course=course.strip(),
                    city=city.strip(),
                    dob=dob_str,
                )
            if ok:
                st.success(f"Student '{name}' saved. {message}")
            else:
                st.error(message)

st.divider()
if st.button("Retry loading any pending JSON records into MySQL"):
    with st.spinner("Checking data/students.json for unloaded records..."):
        ok, message, count = etl_service.load_pending_students_to_db()
    if ok:
        st.info(message)
    else:
        st.error(message)
