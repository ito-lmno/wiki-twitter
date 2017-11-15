from requests_oauthlib import OAuth1Session
import requests
import json
import sys

geturl = 'http://wikipedia.simpleapi.net/api/?keyword=渋谷&output=json&lang=ja&search=0'

r = requests.get(geturl)

print (r.json()[0])

json_dict = r.json()[0]

print('検索したURL：{}'.format(json_dict['url']))



CK = '{TWITTER_CONSUMER_KEY}'
CS = '{TWITTER_CONSUMER_SECRET}'
AT = '{TWITTER_APPLICATION_TOKEN}'
AS = '{TWITTER_APPLICATION_SECRET}'

tweet = '検索したURL：{}'.format(json_dict['url'])

url = "https://api.twitter.com/1.1/statuses/update.json"

params = {"status": tweet }

twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

if req.status_code == 200:
    print ("Success")
    print("Your tweet is")
    print(tweet)
else:
    print ("Failure: %d" % req.status_code)
