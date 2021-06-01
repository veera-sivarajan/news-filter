from data import *
from reddit_news import *
import os

os.remove("/home/veera/Projects/HNFilter/news/news.html")
head = """<!DOCTYPE html>
<html lang="en">
<link rel="stylesheet" href=/home/veera/Projects/HNFilter/news/style.css>
<meta charset="UTF-8">
<meta name="viewport" content="initial-scale=1">
<meta name="HandheldFriendly" content="true">
"""
hn_data = link_and_titles(cleanse(get_data()))
reddit_data = reddit_link_and_titles()

file = open("/home/veera/Projects/HNFilter/news/news.html", "a")
file.write(head)
file.write("<ol>")

def write_links (data):
    for ele in data:
        file.write("<li>")
        news_line = "<a href=\"" + ele[0] + "\">" + ele[1] + "</a>"
        file.write(news_line)
        comment_line = "<a href=\"" + ele[2] + "\" class=\"other\">" + "Comments" + "</a>"
        file.write("\t | \t")
        file.write(comment_line)
        file.write("</li>")
        file.write("\n")

write_links(hn_data)
write_links(reddit_data)

file.write("</ol>")
file.close()

