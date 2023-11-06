import requests

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)
dict_ = response.json()
print(dict_["posts"][0]["tags"][1]["title"])