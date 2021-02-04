#!/usr/bin/python3
"""recursive function that queries reddit API and returns"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns list of titles of articles"""
    try:
        r = requests.get("https://www.reddit.com/r/{}/hot.json".
                         format(subreddit), headers={"User-Agent": "custom"},
                         params={"after": after},
                         allow_redirects=False).json()
    except:
        return None

    if ("data" in r and "children" in r.get("data")):
        """data list tieles of articles"""
        for x in r.get("data").get("children"):
            hot_list.append(x.get("data").get("title"))
        if "after" in r.get("data") and r.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           r.get("data").get("after"))
        else:
            return hot_list
    else:
        return None
