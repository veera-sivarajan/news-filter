from data import *
import os

os.remove("/home/veera/Projects/HNFilter/news/news.html")
head = """<!DOCTYPE html>
<html lang="en">
<link rel="stylesheet" href=/home/veera/Projects/HNFilter/news/style.css>
<meta charset="UTF-8">
<meta name="viewport" content="initial-scale=1">
<meta name="HandheldFriendly" content="true">
"""
data = link_and_titles(cleanse(get_data()))

file = open("/home/veera/Projects/HNFilter/news/news.html", "a")
file.write(head)
file.write("<ol>")

for ele in data:
    file.write("<li>")
    line = "<a href=\"" + ele[0] + "\">" + ele[1] + "</a>"
    file.write(line)
    file.write("</li>")
    file.write("\n")

file.write("</ol>")
file.close()

