# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class FriendManager(models.Manager):
    def addFriend(self, user, friend):
        if len(Friend.objects.filter(owner = user)) == 0:
            Friend.objects.create(owner = user)
        if len(Friend.objects.filter(owner = friend)) == 0:
            Friend.objects.create(owner = friend)
        Friend.objects.get(owner = user).friends.add(friend)
        Friend.objects.get(owner = friend).friends.add(user)

class Friend(models.Model):
    owner = models.ForeignKey(User, null=True)
    friends = models.ManyToManyField(User, related_name="friends")
    date_added = models.DateTimeField(auto_now_add=True)
    objects = FriendManager()