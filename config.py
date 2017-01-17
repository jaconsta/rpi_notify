import os


# Twitter consumer keys and access tokens, used for OAuth
consumer_key = os.environ.get('TWITTER_KEY', '7EyzTcAkINVS3T2pb165')
consumer_secret = os.environ.get('TWITTER_SECRET', 'a44R7WvbMW7L8I656Y4l')
access_token = os.environ.get('TWITTER_TOKEN', 'z00Xy9AkHwp8vSTJ04L0')
access_token_secret = os.environ.get('TWITTER_TOKEN_SECRET', 'A1cK98w2NXXaCWMqMW6p')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DIR = os.path.dirname(os.path.realpath(__file__))
