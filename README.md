# Tech-Blog
This is a simple news blog made for learning purposes. The front-end is made using HTML5, CSS3, JQuery, Bootstrap4. The back-end is made with Django3.

However, the blog is tested in a local server, feel free to upload it into a production server after changing some settings of course.

# Features 
- Usual blog operations (reading, removing, updating an article)
- Users can subscribe so every new released article will be sent to their gmail 
- Comments on posts.
- Tagging, searching, recommendation systems ( currently implementing them) 

# Testing it on a local server 

Clone and download the repository and rename it (whatever you want)

### Installing tinymce4 

If you're a windows user open the cmd, and type the following command: 

``` pip3 install django-tinymce4-lite ```

If you're a linux user:

``` 
sudo apt-get update 
pip3 install django-tinymce4-lite
pip3 install django-tinymce4-widget
```
### Creating the project, the application and some necessary settings 

Open the command line and type the following:

``` django-admin startproject FullBlog ```
and 

``` python manage.py startapp Blog ```

❗❗ Every file in the FullBlog project should be replaced with the corresponding one in this repo. Same folders and files are missing here because django will create them.

❗️ Replace every file in that project you created with the corresponding one in this repo

finally...

```
cd FullBlog 
python3 manage.py makemigrations 
python3 manage.py migrate 

python3 manage.py runserver 
```

### Sending emails to subscribers 

first of all, open the command line and type the following 

``` 
sudo su 
python3 -m smtpd -c DebuggingServer localhost:1025
```

Go to ``` settings.py ```, copy and past the following:
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'your email'  
EMAIL_HOST_PASSWORD = ''        #Make sure to not write it if you're in a production server (use some google APIs)
EMAIL_USE_TLS = True 
```
In your gmail account (EMAIL_HOST_USER), go to ``` https://myaccount.google.com/lesssecureapps ```, turn it on

In case you don't know what's it, it allows third party software to send emails using your account

To get the contact section, check ``` http://127.0.0.1:8000/contact.html ```

# Overview
Emmm, i will add some screenshots later....
