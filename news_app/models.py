from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    image_title = models.ImageField(default="pamant.jpg")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    CHOICE_CATEGORIES = (
        ('FOTBAL', 'Fotbal'),
        ('TENIS', 'Tenis'),
        ('STIRI_EXTERNE', 'Stiri externe'),
        ('HANDBAL', 'Handbal'),
        ('BASKET', 'Basket'),
        ('ALTE_SPORTURI', 'Alte sporturi')
    )
    categories = models.CharField(max_length=200, choices=CHOICE_CATEGORIES, default='Fotbal')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_author(self):
        return self.author

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('news_app.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def get_author(self):
        return self.author

    def get_user_by_author(self):
        user_by_author_name = User.objects.get(username=self.author)
        return user_by_author_name

    def get_post(self):
        return self.post

    def __str__(self):
        return self.text


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
