#!/usr/bin/python3
'''
    This module contains a function that queries the Reddit API and returns the number of subscribers for a given subreddit.
'''
import requests
from sys import argv

def number_of_subscribers(subreddit):
    '''
        This function queries the Reddit API and returns the number of subscribers for a given subreddit.
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=user)

    try:
        return url.json().get('data').get('subscribers')
    except Exception:
        return 0

if __name__ == '__main__':
    number_of_subscribers(argv[1])