import os

from nfty import Ntfy
from pronote import *
from db import *

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

pronote = Pronote(username, password)
db = DB("pronote", "grades")
nfty = Ntfy()

# Fill the database with grades if it's empty
if len(db.get_grades()) == 0:
    db.insert_grades(pronote.get_grades())
    print("Grades inserted")
    exit()

if len(db.get_grades()) == len(pronote.get_grades()):
    print("No new grades")
else:
    # Get the new grades
    new_grades = [grade for grade in pronote.get_grades() if grade["_id"] not in db.get_grades()["_id"].tolist()]
    print(f"Founds {len(new_grades)} new grades")
    # Insert the new grades
    db.insert_grades(new_grades)
    print("New grades inserted")

    # Send the new grades with ntfy
    for new_grade in new_grades:
        content = nfty.set_content(new_grade)
        nfty.send(f"{new_grade['grade']}/{new_grade['out_of']} {new_grade['subject']}", content, "books", "high",
                  "grades")