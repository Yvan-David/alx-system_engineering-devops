#!/usr/bin/python3
"""This script returns the number of subscribers for a
subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit"""
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
        subreddit),
                     headers={'User-Agent': 'reddit/2023.20.0'})
    try:
        posts = r.json().get('data').get('children')
        [print(post.get('data').get('title')) for post in posts[:10]]
    except AttributeError:
        print("None")
