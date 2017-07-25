# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login.models import User
from .models import Friend 
from django.contrib import messages
# Create your views here.
def status(valid, request):
    if not valid:
        messages.error(request, "No hacking! Please log in first")
        return True

def index(request):
    if status(request.session['status'], request):
        return redirect('/')
    context = {
        "three": User.objects.all().order_by('-date_added')[:3]
    }
    return render(request, 'friends/index.html', context)

def add_home(request):
    if status(request.session['status'], request):
        return redirect('/')
    all_friends = Friend.objects.get(owner=User.objects.get(id=request.session['id'])).friends.all()
    exclude = []
    for friend in all_friends:
        exclude.append(friend.id)
    notFriends = User.objects.exclude(id = request.session['id']).exclude(id__in=exclude)

    context = {
        "non_friends": notFriends
    }
    return render(request, 'friends/add_home.html', context)

def add(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    Friend.objects.addFriend(User.objects.get(id = request.session['id']), User.objects.get(id = id))
    return redirect('friends/view')

def view(request):
    if status(request.session['status'], request):
        return redirect('/')
    if len(Friend.objects.filter(owner = User.objects.get(id = request.session['id']))) != 0:
        context = {
            "friends": Friend.objects.get(owner = User.objects.get(id = request.session['id'])).friends.all()
        }
    else:
        context = {
        }
    return render(request, 'friends/view.html', context)

def delete(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    Friend.objects.get(owner = User.objects.get(id = request.session['id'])).friends.remove(User.objects.get(id = id))
    Friend.objects.get(owner = User.objects.get(id = id)).friends.remove(User.objects.get(id = request.session['id']))
    return redirect('/friends/view')