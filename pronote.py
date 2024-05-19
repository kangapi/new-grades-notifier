import hashlib
import json
import os

import pronotepy

class Pronote:
    def __init__(self, username, password):
        self.url = os.getenv('PRONOTE_URL')
        self.client = pronotepy.Client(self.url, username, password)
        self.grades = self.pull_grades()
    def pull_grades(self):
        grades = []
        for period in self.client.periods:
            for grade in period.grades:
                grade_dict = self.format_grade(grade)
                grades.append(grade_dict)
        return grades

    def format_grade(self, grade: pronotepy.Grade):
        grade_dict = grade.to_dict()
        grade_dict['subject'] = grade_dict['subject']['name']
        grade_dict["date"] = str(grade_dict["date"])
        grade_dict.pop("id")
        grade_dict['out_of'] = self.grade_to_int(grade_dict['out_of'])
        grade_dict['grade'] = self.grade_to_int(grade_dict['grade'])

        grade_dict["_id"] = self.generate_grade_id(grade_dict)

        return grade_dict

    def generate_grade_id(self, grade: dict):
        # Convert the dictionary to a JSON string
        grade_json = json.dumps(grade, sort_keys=True).encode()
        # Calculate the SHA-256 hash
        grade_id = hashlib.sha256(grade_json).hexdigest()
        return grade_id

    def grade_to_int(self, string: str):
        try:
            number = float(string.replace(",", "."))
            return number
        except ValueError:
            return None

    def get_grades(self):
        return self.grades