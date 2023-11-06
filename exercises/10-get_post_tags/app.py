import requests

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

def get_post_tags(post_id):
   response = requests.get(url)
   dict_ = response.json()
   tags = []
   for post in dict_["posts"]:
       if post["id"] == post_id:
           tags = post["tags"]
   return tags
            
print(get_post_tags(146))
