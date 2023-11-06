import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"
response = requests.get(url)
    if str(response.status_code) == 404:
    print("The URL you asked is not found")
    if str(response.status_code) == 503:
    print("Unavailable right now")
    if str(response.status_code) == 200:
    print("Everything went perfect")
    if str(response.status_code) == 400:
    print("	Something is wrong on the request params")