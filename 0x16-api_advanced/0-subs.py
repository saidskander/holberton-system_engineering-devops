#!/usr/bin/python3
import requests
"""subscribers"""


def number_of_subscribers(subreddit):
    """ Returns number of subscribers """
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent":
                 "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
    if (r.status_code == 200):
        return r.json().get("data").get("subscribers")
    else:
        return 0
