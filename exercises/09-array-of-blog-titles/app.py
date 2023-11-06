import requests

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

def get_titles():
    titles = []
    response = requests.get(url)
    dict_ = response.json()
    for p in dict_["posts"]:
       titles.append(p["title"])
    return titles

print(get_titles())