"""
database/db_connector.py
Handles all raw connections to MySQL using pymysql.
Provides a context-managed connection and small helper methods
for execute / executemany / fetch so the rest of the app never
has to deal with cursors directly.
"""

import pymysql
import pymysql.cursors
from contextlib import contextmanager
from config.config import config


class DBConnector:
    def __init__(self):
        self.host = config.DB_HOST
        self.port = config.DB_PORT
        self.user = config.DB_USER
        self.password = config.DB_PASSWORD
        self.database = config.DB_NAME

    def _connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False,
            connect_timeout=10,
        )

    @contextmanager
    def get_connection(self):
        """Yields a live connection, always closed afterwards."""
        conn = self._connect()
        try:
            yield conn
        finally:
            conn.close()

    def test_connection(self):
        """Returns (True, message) or (False, error_message)."""
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1")
            return True, "Connection successful"
        except Exception as e:
            return False, str(e)

    def execute(self, query, params=None):
        """Run a single INSERT/UPDATE/DELETE/DDL statement. Commits automatically."""
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params or ())
                conn.commit()
                return cur.lastrowid

    def executemany(self, query, param_list):
        """Bulk insert/update. Commits automatically. Returns rows affected."""
        if not param_list:
            return 0
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                affected = cur.executemany(query, param_list)
                conn.commit()
                return affected

    def fetch_all(self, query, params=None):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params or ())
                return cur.fetchall()

    def fetch_one(self, query, params=None):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params or ())
                return cur.fetchone()


# Single shared instance used across the app
db = DBConnector()
