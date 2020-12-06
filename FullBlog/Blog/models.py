from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.



    
class BlogPost(models.Model):

    title = models.CharField(max_length=100)
    post_category = models.CharField(max_length=25, null=True)

    author = models.CharField(max_length=15)
    content = HTMLField()

    post_slug = models.SlugField()
    date = models.DateTimeField(default=timezone.now())

    number_views = models.IntegerField(default=0)  #number of views 
    post_image = models.ImageField()

    # If the articles is featured elsewhere 
    featured = models.BooleanField(default=False)

    #published or not 
    # When this value is set to true it means all our subscribers had received their news feed
    #when it's set to false it means we should send this articles to our subscribers and then 
    #set it to true 
    published = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'Article'
        ordering = ['-date']

    def __str__(self):

        return self.title


class Subscriber(models.Model):

    email = models.EmailField(max_length=30, blank=False, unique=True)
    user_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.email 

