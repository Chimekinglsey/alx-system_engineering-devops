#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[]):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "RecursiveReddit/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        if not posts:
            return hot_list
        for title in posts:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        print(None)
        return (0)
