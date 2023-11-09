#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ Reddit API endpoint for getting hot posts in a subreddit
        a custom User-Agent to avoid Too Many Requests error
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        posts = data['data']['children']

        for i in range(min(10, len(posts))):
            print(posts[i]['data']['title'])
    elif response.status_code == 404:
        print(None)
    else:
        print(f"Error: {response.status_code}")
