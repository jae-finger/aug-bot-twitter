# Import packages
# import random
import tweepy
import os
from rich import print

# Get Augie Facts
# from augie_facts import augie_facts

# Load Environmental Variables
from dotenv import load_dotenv
load_dotenv()

# Create credentials from environmental variables
consumer_key = os.getenv("TW_CONS_KEY")
consumer_secret = os.getenv("TW_CONS_SEC")
access_token = os.getenv("TW_ACCESS_TOKEN")
access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")


# def AugieFact(consumer_key, consumer_secret, access_token, access_token_secret):
#     """
#     Tweets a random augie fact.
#     """
#     # Set Authentication
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)

#     # Instantiate Tweepy API
#     api = tweepy.API(auth)

#     rand_fact = augie_facts[random.randint(0, len(augie_facts)-1)]
#     print(f'Attempting to tweet fact # {len(augie_facts)-1}')
#     api.update_status(rand_fact)


if __name__ == '__main__':
    print(consumer_key, consumer_secret, access_token, access_token_secret)
#     print('Getting a random fact...')
#     AugieFact(consumer_key, consumer_secret, access_token, access_token_secret)
