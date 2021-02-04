#!/usr/bin/python3
"""prints the titles of the first 10 posts"""
import requests


def top_ten(subreddit):
    """prints the titles"""
    r = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".
                     format(subreddit), headers={"User-Agent": "custom"})

    if (r.status_code == 200):
        for x in r.json().get("data").get("children"):
            print(x.get("data").get("title"))
    else:
        print("None")
