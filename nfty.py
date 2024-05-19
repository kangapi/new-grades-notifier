import locale
import os
from datetime import datetime
import requests

auth = os.getenv("NTFY_AUTH")



class Ntfy:
    def __init__(self):
        self.url = os.getenv("NTFY_URL")
    def send(self, title, content, tags, priority, topic):
        url = f"{self.url}/{topic}?title={title}&tags={tags}"

        payload = content
        print(payload)
        headers = {
            'Priority': priority,
            'Content-Type': 'text/plain',
            'Authorization': auth
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)

    def set_content(self, grade: dict):
        date = datetime.strptime(grade["date"], "%Y-%m-%d")
        content = f"Min → {grade['min']}\nMax → {grade['max']}\nMoyenne → {grade['average']}\nDate → {date.strftime('%x')}\nComment → {grade['comment']}      "
        print(content)
        return content
