"""
app.py
Main entry point for the Streamlit ETL app.
Run with:  streamlit run app.py
"""

import streamlit as st
from database.db_connector import db
from database.models import init_db, count_students, get_recent_logs

st.set_page_config(
    page_title="Student ETL",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Student Data ETL Dashboard")
st.caption("Form entry → JSON (intermediate) → MySQL, using PyMySQL.")

# --- Connection check ---
with st.spinner("Checking database connection..."):
    ok, msg = db.test_connection()

col1, col2 = st.columns(2)
with col1:
    if ok:
        st.success(f"Database connection: {msg}")
    else:
        st.error(f"Database connection failed: {msg}")
        st.info("Check your .env file (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) and that MySQL is running.")

with col2:
    if st.button("Initialize / Verify Tables"):
        try:
            init_db()
            st.success("Tables verified/created: students, etl_log")
        except Exception as e:
            st.error(f"Could not initialize tables: {e}")

st.divider()

# --- Quick stats ---
if ok:
    try:
        total = count_students()
        st.metric("Total students in database", total)
    except Exception as e:
        st.warning(f"Tables may not exist yet. Click 'Initialize / Verify Tables' above. ({e})")

    st.subheader("Recent ETL runs (JSON -> MySQL)")
    try:
        logs = get_recent_logs(10)
        if logs:
            st.dataframe(logs, use_container_width=True)
        else:
            st.info("No ETL runs yet. Go to 'Add Student' in the sidebar to add your first record.")
    except Exception:
        pass

st.divider()
st.markdown(
    """
    ### How this app works
    1. Fill in your MySQL credentials in the **.env** file, then click **Initialize / Verify Tables** above.
    2. Go to **Add Student** (sidebar) and fill out the form.
    3. On submit, the record is first appended to `data/students.json` (the intermediate JSON file),
       then immediately loaded into the MySQL `students` table.
    4. Go to **View Students** (sidebar) to see what's in MySQL, and to peek at the raw JSON file.
    """
)
