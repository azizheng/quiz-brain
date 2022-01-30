import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category":18
}

data = requests.get("https://opentdb.com/api.php", params=parameters)
data.raise_for_status()

question_data = data.json()["results"]
