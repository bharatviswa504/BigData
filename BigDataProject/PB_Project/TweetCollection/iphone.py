import pymongo
from pymongo import MongoClient
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
ckey = 'HiV1yNqUzK8mQQ4syTVcnFVRK'
csecret = 'HlEZ4G7hYfJqQvAzQUj9tLllX4nfn1Hdc3bE8KzjyC8XqL0xcA'
atoken = '2771116699-HpksvxtwTkBmZKbAvYOqHU7aXMXGRGZGCEP9ifA'
asecret = 'AGi7K4OL7ymdV3H3TbnLVfUPiwuebECWZhunOOaVWKpvi'

class listener(StreamListener):
	
	def on_data(self,data):
		try:        
			collection.insert({'tweet':data})
			return True
		except BaseException, e:
			print 'failed writing,', str(e)
			time.sleep(5)
			
	
	def on_error(self, status):
		print status
client = MongoClient('localhost', 27017)
db = client.iphone
collection = db.iphone_tweet_data
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track = ["iphone6" | "iphone5" | "iphone"])

