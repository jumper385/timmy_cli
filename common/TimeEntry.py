from datetime import datetime, timedelta

class TimeEntry:
    def __init__(self, start_time_string, duration_hours = None, end_time_string = None):
        self.start_time_string = start_time_string
        self.duration_hours = duration_hours
        self.end_time_string = end_time_string

    def print_me(self):
        print("HELLO WORLD")
