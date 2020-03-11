from .thumbnail import dl_make_thumbnail
import os
import tweepy
import concurrent.futures
cache=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\","/")+"/Images/Twitter/"


#credentials
class TwitterClient():
    API_key= ""
    API_secret_key=""
    Access_token =""
    Access_token_secret =""

    def __init__(self):
        auth= tweepy.OAuthHandler(self.API_key, self.API_secret_key)
        auth.set_access_token(self.Access_token, self.Access_token_secret)
        self.twitter=tweepy.API(auth)
        self.tweets=self.twitter.home_timeline(exclude_replies=True, count=50)


    def get_images(self): 
        #NSFW filter neeeds to be implemented
        TIndex=[]
        for tweet in self.tweets:
            try:
                #check if tweet has media
                if tweet.entities["media"]:
                    #get media url and tweet link from JSON data
                    for media in tweet.extended_entities["media"]:
                        media_url=media["media_url"]
                        print(media_url)
                        tweet_url=media["url"]
                            
                        #Populate IndexList
                        TIndex.append([media_url, tweet_url])
                else:
                    print("Exception raised;", end=" ")
                    raise Exception
            except:
                print("Not an image")

        return TIndex

    #----------------------------Under Construction--------------------------
    def add_handle(self, *args):
        for handle in args:
            self.tweets=self.twitter.user_timeline(id=handle, exclude_replies=True, count=50)

    def remove_from_feed(self, *args):
        for X in args:
            pass