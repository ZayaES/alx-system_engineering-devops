#!/usr/bin/python3
"""uses recursion to create a list of hot topics in a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """the main function that does the above"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    par = {
            'count': count,
            'after': after,
            'limit': 100
            }
    headers = {
            'User-Agent': 'Boss, na me'
            }

    if subreddit is None or type(subreddit) is not str:
        return None

    response = requests.get(url,
                            headers=headers,
                            params=par,
                            allow_redirects=False)
    response_j = response.json()
    result = response_j['data']
    after = result['after']
    count += result['dist']
    for topic in result['children']:
        hot_list.append(topic['data']['title'])

    if after is not None:
        recurse(subreddit, hot_list, after, count)

    return hot_list
