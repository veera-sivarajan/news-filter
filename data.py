import requests
import json

avoid_words = [ "instagram",
                "facebook",
                "google",
                "twitter",
                "apple",
                "tesla" ]

def get_data ():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    topstories_id = requests.get(url).json()
    result = ["Instagram is the best text editor"]
    for id in topstories_id[0:10]:
        data = requests.get('https://hacker-news.firebaseio.com/v0/item/' +
                        str(id) + '.json?print=pretty').json()
        result.append(data['title'])
    return result

def cleanse (title_list):
    result = [] 
    for title in title_list:
        points = 0
        for word in avoid_words:
            if word not in title.lower():
                points += 1
        if points == len(avoid_words): 
            result.append(title)
    return result

def display_titles (title_list):
    count = 0
    for title in title_list:
        count += 1
        print(str(count) + ".", end = " ")
        print(title)

display_titles(cleanse(get_data()))
