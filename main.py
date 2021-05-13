import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

search = "zerotomastery"
numberOfTweets = 2


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


# Fonction pour follow tous les followers
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Usernamehere':
        print(follower.name)
        follower.follow()

# Fonction pour like ses propres tweets.
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
