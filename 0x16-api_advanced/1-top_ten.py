#!/usr/bin/python3

'''
1-top_ten.py - a function that queries reddit
API and returns first 10 hot posts listed for a given subreddit
'''

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of the first 10 hot posts"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "1-top_ten/1.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts[:10]:
            title = post['data']['title']
            print(title)
    else:
        return (0)
