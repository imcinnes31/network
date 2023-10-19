from django.test import TestCase

# Create your tests here.
from django.test import Client, TestCase

from .models import User, Post
import time

# Create your tests here.
class NetworkTestCase(TestCase):

    def setUp(self):
        # Create 3 users
        u1 = User.objects.create_user(username='testuser1', password='12345')
        u2 = User.objects.create_user(username='testuser2', password='12345')
        u3 = User.objects.create_user(username='testuser3', password='12345')


    def test_valid_follower_list(self):
        # One user follows another (valid)
        u1 = User.objects.get(username='testuser1')
        u2 = User.objects.get(username='testuser2')
        
        u1.usersFollowed.add(u2)

        self.assertTrue(u1.is_valid_follow())

    def test_invalid_follower_list(self):
        # One user follows themselves (invalid)
        u2 = User.objects.get(username='testuser2')

        u2.usersFollowed.add(u2)

        self.assertFalse(u2.is_valid_follow())

    def test_valid_post_like_number(self):
        u1 = User.objects.get(username='testuser1')
        u2 = User.objects.get(username='testuser2')
        u3 = User.objects.get(username='testuser3')

        # A post is created, and two different users like it (valid)
        p = Post.objects.create(user=u1,body="Can you picture that?")
        p.usersLiked.add(u2)
        p.usersLiked.add(u3)

        self.assertEqual(p.get_num_likes(), 2)

    def test_invalid_post_like_number(self):
        u1 = User.objects.get(username='testuser1')
        u2 = User.objects.get(username='testuser2')

        # A post is created, and the same user likes it twice (invalid)
        p = Post.objects.create(user=u1,body="Can you picture that?")
        p.usersLiked.add(u2)
        p.usersLiked.add(u2)

        self.assertEqual(p.get_num_likes(), 1)

    def test_posts_datetime(self):
        u1 = User.objects.get(username='testuser1')

        postArray = []

        p1 = Post.objects.create(user=u1,body="You gotta see it in your mind")
        postArray.insert(0, p1)
        time.sleep(0.001)
        p2 = Post.objects.create(user=u1,body="You know it's quick and easy to find")
        postArray.insert(0, p2)
        time.sleep(0.001)
        p3 = Post.objects.create(user=u1,body="You don't have to buy a frame")
        postArray.insert(0, p3)
        time.sleep(0.001)
        p4 = Post.objects.create(user=u1,body="Can you picture that")
        postArray.insert(0, p4)

        postQuery = Post.objects.all().order_by("-timestamp")

        for x in range(3):
            self.assertEqual(postArray[x],postQuery[x])




    

        



