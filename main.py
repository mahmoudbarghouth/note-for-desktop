
from datetime import date
from pathlib import Path
day=date.today()
day_name=day.strftime("%A").lower()
folder_of_name=Path(day_name)
folder_of_name.mkdir(exist_ok=True)
file=f"{day_name}_{day}.txt"
file_name=folder_of_name / file

days={ "saturday": "Start the week strong!",
    "sunday": "Plan your week ahead.",
    "monday": "Focus on tasks.",
    "tuesday": "Team meeting day.",
    "wednesday": "Halfway there!",
    "thursday": "Wrap up pending work.",
    "friday": "Review and reflect."}

content=f"{day}\nDay:{day_name}\nnote:{days.get(day_name)}"

file_name.write_text(content)
