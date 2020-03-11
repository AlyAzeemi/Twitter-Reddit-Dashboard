from django.shortcuts import render
from django.views import View
from .models import PostWindow
from .twitterbridge import TwitterClient
from .redditbridge import RedditClient

# Create your views here.

class PlatformSelectionView(View):
    template_name="Dashboard.html"

    def get(self, request, *args, **kwargs):
        #Insert Twitter Image->Thumbnail converter which returns a list of (filepaths,tweet URLs) to be operated on
        

        
        object_list=PostWindow.objects.all()
        context={
            "object_list" : object_list
        }
        return render(request, self.template_name, context)




class RedditImageView(View):
    RClient=RedditClient()
    template_name="reddit.html"
    def get(self, request, *args, **kwargs):
        self.RClient.remove_from_multireddit()
        self.get_reddit_content("PrettyGirls")

        sub_list=self.RClient.get_active_subreddits() 
        object_list=PostWindow.objects.filter(post_link__contains="https://www.reddit.com")
        context={
            "object_list" : object_list,
            "sub_list"    : sub_list
        }
        return render(request, self.template_name, context)


    def get_reddit_content(self, *args):
        if args!=None:
            self.RClient.add_to_multireddit(*args)
        RList=self.RClient.get_images()
        queryset=PostWindow.objects.filter(post_link__contains="https://www.reddit.com")

        #Prevent Duplication
        for submission in RList:
            try:
                if queryset.filter(image_path=submission[0]):
                    raise Exception
                P=PostWindow.objects.create(image_path=submission[0], post_link=submission[1])
                P.id
            except:
                print("Duplicate image: "+submission[0])
       
    

    def post(self, request, *arg, **kwargs):
        
        
        if request.POST.get("remove")!=None:
            self.RClient.remove_from_multireddit(request.POST.get("remove")[2:])
            PostWindow.objects.filter(post_link__contains=request.POST.get("remove")[1:]).delete()
        
        self.get_reddit_content(request.POST.get("subs"))

        sub_list=self.RClient.get_active_subreddits() 
        object_list=PostWindow.objects.filter(post_link__contains="https://www.reddit.com")
        context={
            "object_list" : object_list,
            "sub_list"    : sub_list
        }
        return render(request, self.template_name, context)


class TwitterImageView(View):
    template_name="twitter.html"
    def get(self, request, *args, **kwargs):
        self.get_twitter_content()
        object_list=PostWindow.objects.filter(image_path__contains="twimg")
        context={
            "object_list" : object_list
        }
        return render(request, self.template_name , context)


    def get_twitter_content(self):
        TClient=TwitterClient()
        TList=TClient.get_images()
        queryset=PostWindow.objects.filter(image_path__contains="twimg")
        for tweet in TList:
            try:
                if queryset.filter(image_path=tweet[0]).count()>0:
                    raise Exception
                P=PostWindow.objects.create(image_path=tweet[0], post_link=tweet[1])
            except:
                print("Duplicate image: "+tweet[0])

    def post(self, request, *arg, **kwargs):
        
        
        if request.POST.get("remove")!=None:
            self.RClient.remove_from_multireddit(request.POST.get("remove")[2:])
            PostWindow.objects.filter(post_link__contains=request.POST.get("remove")[1:]).delete()
        
        self.get_reddit_content(request.POST.get("subs"))

        sub_list=self.RClient.get_active_subreddits() 
        object_list=PostWindow.objects.filter(post_link__contains="https://www.reddit.com")
        context={
            "object_list" : object_list,
            "sub_list"    : sub_list
        }
        return render(request, self.template_name, context)

    