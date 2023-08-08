#!/usr/bin/python3


'''
0-subs.py - a function that queries reddit
API with total subscribers count as response
'''

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of
    subscribers for the 'programming' subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "0-subs/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
