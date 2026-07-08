# Student Form → JSON → MySQL ETL (Streamlit + PyMySQL)

## Folder structure
```
etl_app/
├── app.py                       # Main dashboard (run this)
├── requirements.txt
├── .env                         # DB credentials (edit this first)
├── config/
│   └── config.py                # Loads .env into a Config object
├── database/
│   ├── db_connector.py          # PyMySQL connection + execute/fetch helpers
│   └── models.py                # students + etl_log tables, insert/query fns
├── services/
│   ├── json_store.py            # Appends form submissions to data/students.json
│   ├── transformer.py           # Cleans records, maps JSON -> DB tuple
│   └── etl_service.py           # Orchestrates JSON -> MySQL load
├── pages/
│   ├── 1_Add_Student.py         # The student entry FORM
│   └── 2_View_Students.py       # View students in MySQL + raw JSON file
├── data/
│   └── students.json            # Auto-created intermediate JSON file
└── hritik/                      # Your personal scratch folder
```

## How the flow works
```
Streamlit form  --submit-->  data/students.json  --ETL load-->  MySQL "students" table
```
Every submitted student is first appended to `data/students.json` with a
`"loaded": false` flag. Right after saving, the app automatically runs the
ETL step, which reads all `loaded: false` records, inserts them into MySQL,
and flips them to `loaded: true` so they're never inserted twice.

## Setup

1. Create the database in MySQL (tables are auto-created, the database itself is not):
   ```sql
   CREATE DATABASE etl_db;
   ```
2. Edit `.env`:
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=etl_db
   DATA_FOLDER=data
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```
5. In the browser: click **Initialize / Verify Tables**, then go to
   **Add Student** (sidebar) and fill out the form.

## Customizing the student fields
- Form fields live in `pages/1_Add_Student.py`.
- Table columns live in `database/models.py` (`CREATE_STUDENTS_TABLE`, `insert_student`, `bulk_insert_students`).
- The JSON <-> DB field mapping lives in `services/transformer.py` (`transform_students`).

Add a new field (e.g. "gender") in all three places and it'll flow through
automatically: form -> JSON -> MySQL.

## Notes
- Every DB call opens a connection, runs the query, and closes it right
  away (see `db_connector.py`), so nothing sits idle and times out.
- Every JSON -> MySQL load attempt is recorded in the `etl_log` table,
  visible on the home dashboard.
- If the app is closed before a load succeeds (e.g. MySQL was down),
  the record stays in `students.json` with `loaded: false` — use the
  "Retry loading any pending JSON records" button on the Add Student
  page, or just resubmit the form once MySQL is back up.
