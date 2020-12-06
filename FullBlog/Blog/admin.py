from django.contrib import admin
from .models import BlogPost, Subscriber
from tinymce.widgets import TinyMCE
from django.db import models 

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'date', 'author', 'number_views', 'post_category', 'featured', 'published')

    search_fields = ('title', 'content')
    
    formfield_overrides = {

        models.TextField: {'widget': TinyMCE()},
    }

class SubscriberAdmin(admin.ModelAdmin):

    list_display = ('email', 'user_name')


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(BlogPost, PostAdmin)
