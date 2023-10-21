import requests
import json


response_API = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
data = json.loads(response_API.text)

question_data = data["results"]

