from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
    usersFollowed = models.ManyToManyField("self", symmetrical=False, related_name="followedUsers") # Other users this user is following

    # Make sure this user is not following themselves
    def is_valid_follow(self):
        return not self.usersFollowed.contains(self)
    
class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.PROTECT, related_name="userPosted")   # User who made this post
    body = models.TextField()   # Content of post
    timestamp = models.DateTimeField(auto_now_add=True) # Date and time this post was made
    usersLiked = models.ManyToManyField(User, blank=True, related_name="usersLiked")    # The users who like this post

    # Get number of likes this post has, according to users who liked it
    def get_num_likes(self):
        return self.usersLiked.count()

    def __str__(self):
        return f"{self.user}: {self.body}"



