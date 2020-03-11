# Twitter+Reddit Dashboard Djnago App
This is a django project that pulls links from your twitter feed and reddit multireddit into a customised
Dashboard/Imageboard of sorts. Made this so I could go through my feeds faster.
This was my first django project so yes it's very clunky.
Even has some clown code where I basically make the django template engine write JS for me LOL

# Instructions
0. Refer to requirements.txt make sure you have the listed packages installed before attempting to integrate/run this
1. Place your API Keys and credentials inside redditbridge.py and twitterbridge.py
2. Add your multireddit and username to the initializer in redditbridge.py. The reddit Imageboard is fully customisable.
   It will add the subreddits you give it via the add form(displayed on the page) into your Multireddit. Clicking on the 
   tag removes the respective subreddit from your multireddit.
3. The twitter section is yet to be made customisable but will work for your feed.
4. Add this to your django project
5. Enjoy?
