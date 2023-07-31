import tweepy
import time

consumer_key, consumer_secret = 'N0TOiwcaGAE7ELqIhSF4Swrtd','l6SqlxWlMz4Jfd83Ply97cXHOjZfP04E0eGQlXZ0wVYQIP2uwy'
access_token, access_token_secret = '1499265859042172929-XS7ARrlOz3LHjIz5g2CB7RV8WFDaIF', 'umoIvSdqkmnTRUP7QWiBovh4wVjpkqMbZjYEqrmrrYjSu'

client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)



query = '#nft'
tweets = client.search_recent_tweets(query=query, max_results=2)


print('Retweet Bot Started!')

for tweets in api.search_tweets(q="iphone", lang="en", rpp=100).items(2):
    try:
        print('Found tweet by @' + tweet.user.screen_name)

        #Publishing retweet
        tweet.favorite()

        #Updating count for each successfull retweet
        print('Retweet #' + str(count) + ' published successfully.')

        #Random wait time
        timeToWait = random.randint(95, 115)
        print("Waiting for "+ str(timeToWait) + " seconds")
        for remaining in range(timeToWait, -1, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rOnwards to next tweet!\n")

    except tweepy.TweepError as e:
        print('Error: ' + e.args[0][0]['message'])
    except StopIteration:
        break

