import requests
import json

url = "https://www.reddit.com/r/emacs/top.json"
data = requests.get(url, headers = {'User-agent': 'your bot 0.1'}).json()

news_list = data['data']['children']

def reddit_link_and_titles ():
    result = []
    for news in news_list:
        temp = []
        temp.append(news['data']['url'])
        temp.append(news['data']['title'])
        result.append(temp)
    return result

# print(reddit_link_and_titles())
