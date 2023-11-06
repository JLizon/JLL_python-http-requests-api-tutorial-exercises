import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"
myjson = {
    "id":2323,
    "title": "Very big project"
    }

response = requests.post(url, json = myjson)
print(response.text)