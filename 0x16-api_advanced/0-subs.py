#!/usr/bin/python3
"""This script returns the number of subscribers for a
subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit"""
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': 'reddit/2023.20.0'})
    if (r.status_code >= 300):
        return (0)
    return (r.json().get('data')['subscribers'])
