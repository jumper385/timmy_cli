import sqlite3
from datetime import datetime
from common.TimeEntry import TimeEntry

class TimeSheet:
    def __init__(self, sq3_path):
        self.sq3_conn = sqlite3.connect(sq3_path)
        self.sq3_cursor = self.sq3_conn.cursor()

        self._create_tables_if_not_exist()

    def insert_time_entry(self, time_entry):
        """
        Insert a time entry object and add it to the database

        Parameters:
            - time_entry (TimeEntry): The time entry object
        """

        cmd = """
        INSERT INTO time_entry (start_ts, duration_sec, end_ts, description, category, client)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        self.sq3_cursor.execute(cmd, (
            time_entry.start_ts,
            time_entry.duration_sec,
            time_entry.end_ts,
            time_entry.note,
            time_entry.category,
            time_entry.client
        ))

        self.sq3_conn.commit()


    def _create_tables_if_not_exist(self):
        """
        creates the following tables
        - time_entry: start_ts (datetime), duration_sec(int), end_ts(datetime), description(string), category(string), client(string)
        """
        cmd = """
        CREATE TABLE IF NOT EXISTS time_entry (
            start_ts DATETIME,
            duration_sec INTEGER,
            end_ts DATETIME,
            description TEXT,
            category TEXT,
            client TEXT
        );
        """
        self.sq3_cursor.execute(cmd)
