# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from ..friends.models import Friend
from django.contrib import messages
# Create your views here.
def index(request):
    request.session['status'] = False
    return render(request, 'login/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['valid']:
        request.session['name'] = User.objects.filter(email = request.POST['email'])[0].first
        return render(request, 'login/success.html')
    else: 
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['valid']:
        request.session['name'] = User.objects.filter(email = request.POST['login_email'])[0].first
        request.session['id'] = User.objects.filter(email = request.POST['login_email'])[0].id
        request.session['status'] = True
        return redirect('/friends')
    else:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')