#!/usr/bin/python3
import requests
"""subscribers"""


def number_of_subscribers(subreddit):
    """number_of_subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent':
                  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data_request = req.get('data')
        subscribers = data_request.get('subscribers')
        if data_request is not None and subscribers is not None:
            return subscribers
    return 0
