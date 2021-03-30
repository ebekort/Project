#!/usr/bin/python3
#
# Author: Ebe Kort
#
# Description:
# This program checks every tweet with a location in the metadata for swear words and counts
# the amount of tweets with swear words for regions with high educated people and regions
# with lower educated people
# Usage: ./swear_words_in_tweets.py Directory_path_with_tweets

import gzip
import os
import json
import sys

# opens the file with all the swear words and makes a list out of it
with open('swear_words.txt') as f:
    inp = f.read()
    swear_words = inp.splitlines()

# oepens the file with all the cities in high educated regions and makes a list
with open('cities.txt') as f2:
    inp2 = f2.read()
    cities = inp2.splitlines()

# setting every counter to 0
high_ed_non_swears = 0
low_ed_non_swears = 0
high_ed_swears = 0
low_ed_swears = 0

# opening file
Path = sys.argv[1]
filelist = os.listdir(Path)
for x in filelist:
    if x.endswith('.gz'):
        with gzip.open(x) as inp:
            # for each tweet convert it to a python dictionary
            for jsonObj in inp:
                    tweet = json.loads(jsonObj)
                    # checks whether there is a location or not
                    if tweet['user']['location'] != None:
                        # checks whether there are any swear words and in what education category each tweet belongs
                        for word in swear_words:
                            if word in tweet['text']:
                                if tweet['user']['location'].lower() in cities:
                                    high_ed_swears += 1
                                else:
                                    low_ed_swears += 1
                                break
                            else:
                                if tweet['user']['location'].lower() in cities:
                                    high_ed_non_swears += 1
                                else:
                                    low_ed_non_swears += 1
                                    
print('high educated tweets with swear words ' + str(high_ed_swears))
print('high educated tweets without swear words ' + str(high_ed_non_swears))
print('low educated tweets with swear words ' + str(low_ed_swears))
print('low educated tweets without  swear words ' + str(low_ed_non_swears))
