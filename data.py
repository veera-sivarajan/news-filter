import requests
import json

avoid_words = [ "instagram",
                "facebook",
                "google",
                "twitter",
                "apple",
                "uber",
                "microsoft",
                "bitcoin",
                "crypto",
                "cryptocurrency",
                "whatsapp",
                "amazon",
                "tesla" ]

def get_data ():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    topstories_id = requests.get(url).json()
    result = []
    for id in topstories_id[0:10]:
        data = requests.get('https://hacker-news.firebaseio.com/v0/item/' +
                            str(id) + '.json?print=pretty').json()
        result.append(data['title'])
    return result

def cleanse (title_list):
    def helper (title):
        points = 0
        for word in avoid_words:
            if word not in title.lower():
                points += 1
        if points == len(avoid_words):
            return True 
        else:
            return False
    return filter(helper, title_list)

def display_titles (title_list):
    count = 0
    for title in title_list:
        count += 1
        print(str(count) + ".", end = " ")
        print(title)

display_titles(cleanse(get_data()))
