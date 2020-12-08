from django.shortcuts import render, redirect
from django.http import request, Http404
from Blog.models import BlogPost, Subscriber, Comment
from django.utils import timezone
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import _thread
import sys
# Create your views here.

def home_page(request):

    # Most read articles
    articles = BlogPost.objects.order_by('-number_views')[:4]

    #featured posts 
    featured_posts = BlogPost.objects.filter(featured=True)

    #recent posts 
    recent_posts = BlogPost.objects.order_by('-date')[:6]

    #top 10 posts 
    top_ten = BlogPost.objects.filter(title__contains="Top 10")
    context = {'articles':articles, 'featured_posts':featured_posts, 'recent_posts':recent_posts, 'top_ten':top_ten}

    return render(request, 'blog/index.html', context)


def view_post(request, post_id):

    """
    A function to view a single post by clicking on its title 
    """

    try:

        post = BlogPost.objects.get(id=post_id)
        post.number_views += 1
        post.save()

        #get the most read articles 
        articles = BlogPost.objects.order_by('-number_views')[:4] #get the most 4 read articles 

        #getting article's comments 
        comments = post.comments.filter(active=True)
        if (request.method == "POST"):

            name = request.POST['user-name']
            email = request.POST['user-email']
            body = request.POST['comment-body']

            new_comment = Comment(post=post,
                                  name=name,
                                  email=email,
                                  body=body
                                )
            
            new_comment.save()
        context = {'post': post, 'articles':articles, 'comments':comments}
        return render(request, 'blog/viewpost.html', context)

    except BlogPost.DoesNotExist:
        raise Http404


def view_category(request, category_name):

    """
    a function to show all the articles of a specific category (given as the parameter)
    """
    try:

        posts = BlogPost.objects.filter(post_category__contains=category_name)
        context = {'posts':posts}
        category = category_name
        return render(request, 'blog/category.html', locals())

    except BlogPost.DoesNotExist:
        raise Http404



def contact(request):

    if (request.method == "POST"):

        name = request.POST['user-name']
        user_email = request.POST['user-email']

        # Add a new use to the database
        new_user = Subscriber(email=user_email, user_name=name)
        new_user.save()

        # if the form is valid 
        if (name) and (user_email):

            return HttpResponseRedirect('/home')

        # The form is invalid 
        else:

            return HttpResponse('Invalid form fields!')

    return render(request, 'blog/contact.html', locals())


def send_feed(request):

    
    unpublished_posts = BlogPost.objects.filter(published=False)

    user_emails = [] 
    subscribed_users = Subscriber.objects.all()

    # Get the users' emails
    for user in (subscribed_users):
        
        user_emails.append(user.email)

    # Sending the feed to our users
    try:

        for post in (unpublished_posts):

            send_mail(post.title, post.content, 'gaouaoui.197@gmail.com', user_emails)
            post.published = True
            post.save()

    except BadHeaderError:
        return HttpResponse('Inavlid header found')


try:

    _thread.start_new_thread(send_feed, (request,))

except Exception as exc:

    print('Cannot start thread')
    sys.exit(1)


