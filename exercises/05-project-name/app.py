import requests

url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url)
dict_ = response.json()

print(dict_["name"])
