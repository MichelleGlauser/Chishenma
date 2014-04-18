from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    category_label = models.CharField(max_length=200)
    category_img = models.ImageField(upload_to='images/', null=True, blank=True)
    category_tag = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.category_label

# class Tag(models.Model):

class Dish(models.Model):
    dish_name_en = models.CharField(max_length=30)
    dish_name_cn = models.CharField(max_length=30)
    dish_img = models.ImageField(upload_to='images/', null=True)
    dish_cuisine = models.CharField(max_length=30)
    dish_course = models.CharField(max_length=30)
    dish_price = models.IntegerField()
    dish_last_reviewed = models.DateTimeField()
    dish_similar = models.CharField(max_length=30) # How will this work? Maybe to ID?

    menu = models.ManyToManyField('Menu')

    def __unicode__(self):
        return self.dish_name_en

class Menu(models.Model):
    menu_price = models.IntegerField()
    menu_num_people = models.IntegerField()
    menu_tags = models.CharField(max_length=200) # How will this work?
    menu_date = models.DateTimeField()

    # def __unicode__(self):
    #     return self.name

class Review(models.Model):
    review_text = models.CharField(max_length=400)
    review_date = models.DateTimeField()

    restaurant = models.ForeignKey('Restaurant')

    # def __unicode__(self):
    #     return self.name

class Restaurant(models.Model):
    rest_name_en = models.CharField(max_length=50)
    rest_name_cn = models.CharField(max_length=50)
    rest_branch = models.CharField(max_length=50)
    rest_other_branches = models.CharField(max_length=400) # How will this work?
    rest_img = models.ImageField(upload_to='images/', null=True)
    rest_desc = models.CharField(max_length=100)
    rest_dianping_id = models.IntegerField()
    rest_latlong = models.CharField(max_length=100) # Store them together in a charfield, in the order google maps likes. split apart if needed, but how?
    rest_address = models.CharField(max_length=100)
    rest_district = models.CharField(max_length=50)
    rest_city = models.CharField(max_length=50)
    rest_phone = models.CharField(max_length=30) # With a custom validation method
    rest_hours = models.CharField(max_length=100)
    rest_url = models.CharField(max_length=100)
    rest_map_url = models.CharField(max_length=200, null=True)

    category = models.ForeignKey(Category)
    dish = models.ForeignKey(Dish)
    menu = models.ForeignKey(Menu)
    rest_bookmarked_users = models.ForeignKey(User)
    # OR with customized Foodie do the following?:
    # rest_bookmarked_users = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.rest_name_en

# class FoodieManager(BaseUserManager):
#     def create_user(self, user_wechat, password):
# 	    user = self.create_user(user_wechat, password=password)
# 	    user.save()
# 	    return user

# class Foodie(AbstractBaseUser):
#     user_wechat = models.CharField(max_length=50, unique=True)
#     # user_password = models.
#     user_city = models.CharField(max_length=25)
#     # user_id = # this is the real order of sign up 
#     user_waitlist_status = models.BooleanField(default=False)
#     user_waitlist_num = models.IntegerField()
#     user_num_referrals = models.IntegerField()

#     user_friend_wechat_ids = models.ForeignKey('Foodie') #need a friend table?
#     user_bookmark_id = models.ForeignKey('Bookmark')
#     reviewer = models.ForeignKey('Review')

#     USERNAME_FIELD = 'user_wechat'
#     REQUIRED_FIELDS = []

#     objects = FoodieManager()

#     # def get_absolute_url(self):
#  #        return "/users/%s/" % urlquote(self.user_wechat)

#     def email_user(self, subject, message, from_email=None):
#         # Sends an email to this user.
#         send_mail(subject, message, from_email, [self.email])

class Bookmark(models.Model):
    bookmark_rest_id = models.IntegerField()
    bookmark_tags = models.CharField(max_length=100)
    bookmark_notes = models.CharField(max_length=200)
    bookmark_img = models.ImageField(upload_to='user/images/', null=True)

    def __unicode__(self):
        return self.name

# class SettingsBackend(object):