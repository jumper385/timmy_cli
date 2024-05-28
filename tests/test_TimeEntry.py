from datetime import datetime, timedelta
import pytest
from common.TimeEntry import TimeEntry

@pytest.mark.parametrize("date_entry, intended_date", [
    ('yesterday', datetime.now() - timedelta(days=1)),
    ('today', datetime.now()),
    ('last week', datetime.now() - timedelta(days=7))
    ('last fortnight', datetime.now() - timedelta(days=14))
    ('3 days ago', datetime.now() - timedelta(days=3)),
    ('4 days ago', datetime.now() - timedelta(days=4)),
    ('2 weeks ago', datetime.now() - timedelta(days=14)),
    ('3 weeeks ago', datetime.now() - timedelta(days=21)),
    ('12/8/24', datetime.strptime("12/08/24", "%d-%m-%y")),
    # '12/08/24',
    # '13/08/2024'
])

def test_create_time_entry_with_dates(date_entry, intended_date):
    """
    The script, when inputting time entries, must parse the following
    strings into start and end dates
    - yesterday
    - today
    - last week
    - last fortnight
    - N days ago
    - N weeks ago
    - DD/M/YY
    - DD/MM/YYYY
    """
    print(intended_date)
