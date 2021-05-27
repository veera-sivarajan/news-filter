import requests
import json

json_data = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()

for id in json_data[0:10]:
    data = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json?print=pretty').json()
    print(data['title'])

