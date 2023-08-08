#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list):
    """count wordlist"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "RecursiveReddit/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')

        if not posts:
            return

        word_count = {}
        for post in posts:
            title = post.get('data').get('title')
            for word in word_list:
                if f" {word.lower()} " in f" {title.lower()} ":
                    word_count[word.lower()] = \
                                word_count.get(word.lower(), 0) + 1

        sorted_results = sorted(word_count.items(),
                                key=lambda x: (-x[1], x[0]))
        for word, count in sorted_results:
            print(f"{word}: {count}")

        after = data['data']['after']
        return count_words(subreddit, word_list)
    else:
        return None
