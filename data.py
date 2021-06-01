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
                "tesla",
                "ios" ]

def get_data ():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    topstories_id = requests.get(url).json()
    result = []
    for id in topstories_id[0:10]:
        data = requests.get('https://hacker-news.firebaseio.com/v0/item/' +
                            str(id) + '.json?print=pretty').json()
        result.append(data)
    return result

def cleanse (news_list):
    def helper (news_object):
        lower_title = news_object['title'].lower()
        for word in avoid_words:
            if word in lower_title: 
                return False
        return True

    return filter(helper, news_list)

def link_and_titles (news_list):
    result = []
    for news in news_list:
        if (news['by'] != "whoishiring"):
            temp = []
            temp.append(news['url'])
            temp.append(news['title'])
            head = "https://news.ycombinator.com/item?id="
            tail = str(news['id'])
            comment = head + tail
            temp.append(comment) # comments
            result.append(temp)
    return result

