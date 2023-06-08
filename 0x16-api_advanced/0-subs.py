#!/usr/bin/python3
"""Module that access the reddit through api."""

import requests


def number_of_subscribers(subreddit):
    """Function that returns number of subcribers of a subreddit."""

    header = {'User-Agent': 'reddit/2023.20.0'}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': 'reddit/2023.20.0'})
    if (r.status_code >= 300):
        return (0)
    return (r.json().get('data')['subscribers'])
