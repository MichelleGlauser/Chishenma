from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from geoposition.fields import GeopositionField

class Category(models.Model):
    category_label = models.CharField(max_length=200)
    category_img = models.ImageField(upload_to='images/', null=True, blank=True)
    category_tag = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.category_label

# class Tag(models.Model): # Do I need this to have multiple tags?

class Dish(models.Model):
    dish_name_en = models.CharField(max_length=30)
    dish_name_cn = models.CharField(max_length=30, blank=True)
    dish_img = models.ImageField(upload_to='images/', null=True, blank=True)
    dish_cuisine = models.CharField(max_length=30)
    dish_course = models.CharField(max_length=30, blank=True)
    dish_price = models.IntegerField(blank=True)
    dish_last_reviewed = models.DateTimeField(blank=True)
    dish_similar = models.CharField(max_length=30, blank=True) # How will this work?

    menu = models.ManyToManyField('Menu')

    def __unicode__(self):
        return self.dish_name_en
        
class Restaurant(models.Model):
    rest_name_en = models.CharField(max_length=50)
    rest_name_cn = models.CharField(max_length=50, blank=True)
    rest_branch = models.CharField(max_length=50, blank=True)
    rest_other_branches = models.CharField(max_length=400, blank=True) # How will this work?
    rest_img = models.ImageField(upload_to='images/', null=True, blank=True)
    rest_desc = models.CharField(max_length=100)
    rest_dianping_id = models.IntegerField(null=True, blank=True)
    rest_position = GeopositionField(null=True) 
    # rest_latlong = models.CharField(max_length=100, blank=True) # Store them together in a charfield, in the order google maps likes. split apart if needed, but how?
    rest_address = models.CharField(max_length=100)
    rest_district = models.CharField(max_length=50)
    rest_city = models.CharField(max_length=50)
    rest_phone = models.CharField(max_length=30) # With a custom validation method
    rest_hours = models.CharField(max_length=100, blank=True)
    rest_url = models.CharField(max_length=100, blank=True)
    rest_map_url = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    rest_dishes = models.ForeignKey(Dish, null=True, blank=True)
    bookmarked_by = models.ForeignKey(User, null=True, blank=True) # Users who have bookmarked a restaurant
    rest_menu = models.ForeignKey('Menu', null=True, blank=True)

    def __unicode__(self):
        return self.rest_name_en

class Menu(models.Model):
    menu_price = models.IntegerField()
    menu_num_people = models.IntegerField()
    menu_tags = models.CharField(max_length=200) # How will this work?
    menu_date = models.DateTimeField()

    # menu_rest = models.ForeignKey('Restaurant')
    # def __unicode__(self):
    #     return self.name

class Review(models.Model):
    review_text = models.CharField(max_length=400)
    review_date = models.DateTimeField()

    restaurant = models.ForeignKey('Restaurant')
    reviewer = models.ForeignKey(User) # Is this in the right place?

    # def __unicode__(self):
    #     return self.name

class Foodie(models.Model):
    user_wechat = models.OneToOneField(User)

    # extended models for the User
    user_city = models.CharField(max_length=25)
    user_waitlist_status = models.BooleanField(default=False)
    user_waitlist_num = models.IntegerField(blank=True)
    user_num_referrals = models.IntegerField(blank=True)

    USERNAME_FIELD = 'user_wechat'
#     user_friend_wechat_ids = models.ForeignKey('Foodie') # Do we need a friend table for this?

#     # def get_absolute_url(self): # What does this do?
#  #        return "/users/%s/" % urlquote(self.user_wechat)

#     def email_user(self, subject, message, from_email=None): # Does this work?
#         # Sends an email to this user.
#         send_mail(subject, message, from_email, [self.email])

def __unicode__(self):
    return self.user_wechat.username

class Bookmark(models.Model):
    bookmark_rest_id = models.IntegerField()
    bookmark_tags = models.CharField(max_length=100)
    bookmark_notes = models.CharField(max_length=200)
    bookmark_img = models.ImageField(upload_to='user/images/', null=True, blank=True)

    bookmarker = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

# class SettingsBackend(object): # Do I need this with the customized User?