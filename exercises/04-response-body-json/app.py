import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
dict_ = response.json()
print("Current time:", dict_['hours'],"hrs", dict_['minutes'], "min and", dict_['seconds'], "sec")