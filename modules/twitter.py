"""
Handles the twitter connection logic.
"""

import tweepy

import config


def twitter_api():
    """
    Authenticate and initialize the Twitter api.

    :return: Twitter API
    """
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)

    api = tweepy.API(auth)
    return api


def tweet_image(image, message):
    """
    Send the message with a file attached.

    :param image: Image url
    :param message: Message
    :return:
    """
    api = twitter_api()
    api.update_with_media(image, status=message)
