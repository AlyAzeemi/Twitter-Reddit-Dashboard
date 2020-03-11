import praw
import re
import os
from pprint import pprint

class RedditClient():
    
    def __init__(self):
        self.reddit=praw.Reddit(
            client_id="",
            client_secret="",
            password="",
            user_agent="",
            username=""
            )
        self.MRedd=None

    def add_to_multireddit(self, *args):
        #Initiate MultiReddit/Custom feed from which we will pick
        if args:
            self.MRedd= self.reddit.multireddit("InsertUsernameHere","Insert Customizable MultiReddit Name Here")
            for subred in args:
                self.MRedd.add(subred)
        else:
            self.MRedd=self.reddit.multireddit("InsertUsernameHere","Insert Backup Static Multireddit Name Here")

    def get_images(self):
        feed= self.MRedd.new(limit=30)

        RIndex=[]
        for submission in feed:
            try:
                pprint(submission)
                exit()
                im_url=submission.url
                print(im_url)

                #Seperate filename from hyperlink
                separation_index=im_url.rfind("/")+1
                filename=im_url[separation_index:]

                #Check if image/video
                if filename=="":
                    raise Exception

                #Populate IndexList
                baseURL="https://www.reddit.com"
                RIndex.append(( im_url , baseURL+submission.permalink ))

            except:
                print("Not an image")


        return RIndex

    def get_active_subreddits(self):
        return self.MRedd.subreddits

    def remove_from_multireddit(self, *args):
        if args==None:
            SRArr=self.get_active_subreddits()
            for sr in SRArr:
                self.MRedd.remove(sr)
                print(f"Removed: {sr}")
        else:
            for SR in args:
                self.MRedd.remove(SR)
                print(f"Removed: {SR}")

