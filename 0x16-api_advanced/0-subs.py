#!/usr/bin/python3
""" gets the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for subreddit"""

    if subreddit is None or type(subreddit) is not str:
        return 0
    data = requests.get('https://www.reddit.com/r/{}/about.json'.format(
                                                                subreddit),
                        headers={'User-Agent': 'Boss, na me'})
    data_j = data.json()
    no_subs = data_j.get('data', {}).get('subscribers', 0)

    return no_subs
