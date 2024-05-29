import subprocess
import pytest
import sqlite3

from common.TimeEntry import TimeEntry
from common.TimeSheet import TimeSheet
from common.DBHolder import DB

@pytest.fixture(scope="function")
def db():
    db_obj = DB("delete_test.db")
    yield db_obj
    db_obj.delete()

def test_create_db(db):
    """
    the database object must be created when the object is created and no file is present
    """
    timesheet = TimeSheet(db.path)
    if not db.exists:
        pytest.fail(f"Module failed to create {db_path}")

@pytest.mark.parametrize('table_name', ["time_entry"])
def test_check_db_tables(db, table_name):
    """
    The database must check which tables are present.
    """
    timesheet = TimeSheet(db.path)

    cmd = """
    SELECT name FROM sqlite_master WHERE type='table' AND name=?;
    """
    db.cursor.execute(cmd, (table_name, ))
    result = db.cursor.fetchone()
    if not result:
        pytest.fail(f"Table {table_name} wasnt created...")

@pytest.mark.parametrize("table_name", ["time_entry"])
@pytest.mark.parametrize("start_date, start_time, end_date, end_time, note", [
    ("today","lunch", "tomorrow","lunch", "THIS IS A NOTE")
])
def test_create_db_entry(db, table_name, start_date, start_time, end_date, end_time, note):

    timesheet = TimeSheet(db.path)
    time_entry = TimeEntry(start_date, start_time, end_date, end_time, note)

    timesheet.insert_time_entry(time_entry)

    result = db.find(table_name, "description", note)
    assert len(result) == 1, "Failed to create an entry"
