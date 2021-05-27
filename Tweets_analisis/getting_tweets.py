import credentials
import tweepy
from datetime import date
import time

def search(query,language):
    auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(f'{tweet.user.screen_name}:\n{tweet.text}\n{"*"*60}')

    today = date.today()
    if today.month < 10:
        month = '0'+str(today.month)

    today = str(today.year)+'-'+month+'-'+str(today.day)
    day = 'tweets(05-'+str(today.day)+').txt'
    id = None
    # id = 1396196996965408777
    count = 0
    while count <= 2000:
        tweets = api.search(q=query, lang=language, tweet_mode='extended', 
        max_id=id ,since=today)#,until='2021-05-25')
        for tweet in tweets:
            if tweet.full_text.startswith('RT'):
                count += 1
                continue
            f = open(day, 'a', encoding='utf-8')
            f.write(tweet.full_text + '\n')
            f.close
            count += 1
            
        id = tweet.id
        print(count)
        print(id)
        time.sleep(7)

def main():
    # a = input('Tema:')
    # b = input('Lenguage: ')
    a = 'bitcoin'
    b = 'es'
    search(a,b)

if __name__ == '__main__':
    main()
