import requests

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

def get_attachment_by_id(attachment_id):
    response = requests.get(url)
    dict_ = response.json()
    attachment_id = []
    for post in dict_["posts"]:
        for attachment in post["attachments"]:
            if attachment["id"] == attachment_id:
             return attachment["title"]
print(get_attachment_by_id(137))
