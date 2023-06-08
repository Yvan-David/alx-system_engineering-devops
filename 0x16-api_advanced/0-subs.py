#!/usr/bin/python3
"""Module that access the reddit through api

This is a script that check subreddit's subscribers.

This file can also be imported as a module and contains the following
function:
    * number_of_subscribers - returns number of subreddit subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Function that returns number of subcribers of a subreddit

    Parameters
    ----------
    subreddit : str
        name of a subreddit

    Returns
    -------
    number of subscribers
        if the subreddit exists
    """

    header = {'User-Agent': 'reddit/2023.20.0'}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': 'reddit/2023.20.0'})
    if (r.status_code >= 300):
        return (0)
    return (r.json().get('data')['subscribers'])
