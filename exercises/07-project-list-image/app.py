import requests

url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
dict_ = response.json()
print(dict_["posts"])
