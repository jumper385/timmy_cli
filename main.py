#! ./venv/bin/python3
import typer
from common.TimeEntry import TimeEntry
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def timmy_enter(
        start_date_string: Annotated[str, typer.Option("--start-date", "-sd", prompt=True)],
        start_time_string: Annotated[str, typer.Option("--start-time", "-st", prompt=True)],
        description: Annotated[str, typer.Option("--desc", "-d", prompt=True)]
        ):

    time_entry = TimeEntry(start_date_string, start_time_string)
    time_entry.set_note(description)

    task_end_type = typer.prompt("Use Duration (d) or End Time (t)")
    if task_end_type == "d":
        duration_string = typer.prompt("Duration of Work")
        time_entry.set_duration(duration_string)
    elif task_end_type == "t":
        end_date = typer.prompt("End Date")
        end_time = typer.prompt("End Time")
        time_entry.set_end_ts(end_date, end_time)

    table = Table("start date", "start time", "duration", "end date", "end time", "description")
    start_date = time_entry.start_ts.strftime("%d-%m-%y")
    start_time = time_entry.start_ts.strftime("%H:%M")

    duration_hrs = str(round(time_entry.duration_sec / 3600, 5))

    end_date = time_entry.end_ts.strftime("%d-%m-%y")
    end_time = time_entry.end_ts.strftime("%H:%M")

    table.add_row(start_date, start_time, duration_hrs, end_date, end_time, time_entry.note)
    console.print(table)

if __name__ == "__main__":
    app()
