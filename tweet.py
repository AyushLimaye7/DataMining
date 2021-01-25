from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json
from pprint import pprint
import tokens

class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag):
        print("Start")
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(tokens.CONSUMER_TOKEN,tokens.CONSUMER_TOKEN_SECRET)
        auth.set_access_token(tokens.ACCESS_TOKEN,tokens.ACCESS_TOKEN_SECRET)
        print("All token set")
        print("Setting up conncetion")
        stream = Stream(auth , listener, tweet_mode = 'extended')
        print("Conncetion setup")
        print("Start Tweeting") 
        stream.filter(track = hash_tag)

class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.count = 0
        self.limit = 100

    def on_data(self, data):
        client = MongoClient()
        db = client.tweets
        tweet_collection = db.tweetCollection
        try:
            new_data = json.loads(data)
            tweet_text = new_data[extended_tweet[full_text]]
            if(!tweet_text.startsWith("RT"))
                ir = tweet_collection.insert_one(new_data)
            # print(ir)
            # qr = tweet_collection.find_one({})
            # pprint(qr)
                with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
                # print(self.count)
                self.count+=1
                if(self.count < self.limit):
                    return True
                else:
                    tweet_collection = db.tweetCollection
                    tweet_collection.create_index([("text", "text")])
                    qr = tweet_collection.find({"$text": {"$search": "music"} } , {"score" : { "$meta": "textScore"}})
                    print(tweet_collection.count())
                    print( qr.count())
        # .sort( {"score" : { "$meta": "textScore"}} )

                return False

        except BaseException as e:
            print("Error")
            print(e)
            exit()
        return True

    def on_error(self, status):
        print(status)
        
if __name__=="__main__":
    
    hash_tag = ["Justin Bieber"]
    fetched_tweets_filename = "justin_beiber_tweets_1.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag)

    # db_collection = DbCollection()
    # db_collection.filter_out()


        
            


