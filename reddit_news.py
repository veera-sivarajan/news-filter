import requests
import json

url = "https://www.reddit.com/r/emacs/top.json"
data = requests.get(url, headers = {'User-agent': 'your bot 0.1'}).json()

news_list = data['data']['children']

for news in news_list:
    print(news['data']['title'])
