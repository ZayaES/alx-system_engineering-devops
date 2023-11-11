#!/usr/bin/python3
""" gets the top 10 hot topics on a subreddit"""
import requests


def top_ten(subreddit):
    """returns the top ten topic"""

    if subreddit is None or type(subreddit) is not str:
        return None
    data = requests.get('https://www.reddit.com/r/{}/hot/.json'.format(
                                                             subreddit),
                        headers={'User-Agent': 'Boss, na me'},
                        params={'limit': 10},
                        allow_redirects=False)

    if data.status_code == 404:
        print(None)
        return

    data_j = data.json()
    topic_data = data_j['data']['children']
    [print(c['data']['title']) for c in topic_data]
