# Project
Final Project for the course Research Methods

# Description
In this project I researched the amount of tweets with swear words between groups with high educated people and groups with lower educated people

# Data
The data is from the karora server from the University of Groningen.
To get this data simply make the download_files.sh program runable with chmod +x and run it with ./download_files.sh
The program will ask you for your credentials and downloads the files.

# Methods
With python I uncompressed the files using gzip module and converted each tweet with the json module.
Once this was done I checked whether a tweet had an location or not.
If the tweet had a location I checked whether there were any swear words in the text or not using swear_words.txt.
After that tweets were distinghuised between high educated regions and lower educated regions using the cities.txt files which contains cities with a high percentage of high educated people.

To use the python program you need to make ./swear_words_in_tweets.py runable with chmod +x.
run it with ./swear_words_in_tweets.py Tweets_directory where Tweets_directory is the directory where the downloaded tweets are at.
