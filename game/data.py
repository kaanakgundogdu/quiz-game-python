import requests

question_type = {
    "amount": 10,
    "type": "boolean"
}

resp = requests.get("https://opentdb.com/api.php", params=question_type)
question_data = {

}
question_data = resp.json()["results"]
