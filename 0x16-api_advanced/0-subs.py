#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """ Reddit API endpoint for getting subreddit information
        and a custom User-Agent to avoid Too Many Requests error
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        subscribers = data['data']['subscribers']

        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0
