# Import packages
import random
import tweepy
import os
from rich import print
from datetime import date

# Get Augie Facts
from augie_facts import text_facts

# Load Environmental Variables
from dotenv import load_dotenv

load_dotenv()

# Create credentials from environmental variables
consumer_key = os.getenv("TW_CONS_KEY")
consumer_secret = os.getenv("TW_CONS_SEC")
access_token = os.getenv("TW_ACCESS_TOKEN")
access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")


def tweet_augie_fact(consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Tweets a random augie fact.
    """
    # Set Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Instantiate Tweepy API
    api = tweepy.API(auth)

    rand_fact = text_facts[random.randint(0, len(text_facts) - 1)]
    print(f"Attempting to tweet fact # {len(text_facts)-1}")
    
    try:
        api.update_status(rand_fact)
        print(f"Successfully tweeted fact # {len(text_facts)-1}")
    except:
        print(f"Failed to tweet fact # {len(text_facts)-1}")


if __name__ == "__main__":
    tweet_augie_fact(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
