#!/bin/bash
# Author: Ebe Kort
#
# Description:
# Downloads all the files that I used in my research from the University of Groningen

# Gets username and password
echo username please
read USERNAME
echo password please
echo In what directory do you want to download your files?
read DIRECTORY

# connects with sever and downloads files
scp $USERNAME@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2021/03/20210328:*.out.gz $DIRECTORY

scp $USERNAME@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2021/02/20210211:*.out.gz $DIRECTORY

scp $USERNAME@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2021/05/20210504:*.out.gz $DIRECTORY

scp $USERNAME@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2021/05/20210524:*.out.gz $DIRECTORY
