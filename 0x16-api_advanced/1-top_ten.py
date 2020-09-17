#!/usr/bin/python3
"""
A function that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the top 10 hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    param = {'limit': 10}
    header = {'user-agent': 'betty_hbtn'}
    r = requests.get(url, headers=header)

    if r.status_code is not 200:
        print('None')
    elif 'data' not in r.json():
        print('None')
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
