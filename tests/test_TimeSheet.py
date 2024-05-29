import subprocess
import pytest
import sqlite3

from common.TimeSheet import TimeSheet
from common.DBHolder import DB

@pytest.fixture
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
