#! ./venv/bin/python3
from common.TimeEntry import TimeEntry

def main():
    print("Hello world")
    timeEntry = TimeEntry('a','b','c')
    timeEntry.print_me()

if __name__ == "__main__":
    main()
