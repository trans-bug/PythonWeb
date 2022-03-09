from urllib import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
'''
# Create your views here.
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User

from django.db.models import Count

from django.views.generic import UpdateView
from django.utils import timezone

from django.utils.decorators import method_decorator

from django.views.generic import ListView

# Create your views here.
'''
class storehome:
    def store_homepage(request):
        
        return HttpResponse(request, 'storehome.html')
    
    

    