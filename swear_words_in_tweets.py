import gzip
import os
import json


with open('swear_words.txt') as f:
    inp = f.read()
    swear_words = inp.splitlines()

with open('cities.txt') as f2:
    inp2 = f2.read()
    cities = inp2.splitlines()

tweets = 0
high_ed_swears = 0
low_ed_swears = 0

Path = '.'
filelist = os.listdir(Path)
for x in filelist:
    if x.endswith('.gz'):
        with gzip.open(x) as inp:
            for jsonObj in inp:
                    tweet = json.loads(jsonObj)
                    if tweet['user']['location'] != None:
                        print(tweets, high_ed_swears, low_ed_swears, x)
                        for word in swear_words:
                            if word in tweet['text']:
                                if tweet['user']['location'].lower() in cities:
                                    high_ed_swears += 1
                                else:
                                    low_ed_swears += 1
                                break
                        tweets += 1
