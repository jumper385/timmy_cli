#! ./venv/bin/python3
from common.TimeEntry import TimeEntry

def main():
    time_entry = TimeEntry('today', 'now')
    time_entry.set_duration("32min+1.223hr+24.3333213sec")
    time_entry.set_end_ts("tomorrow", "3pm")
    print(time_entry)

if __name__ == "__main__":
    main()
