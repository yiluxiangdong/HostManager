#coding:utf-8
from django.http import JsonResponse
from django.shortcuts import render_to_response,redirect,HttpResponse,render,HttpResponseRedirect
from .models import *
import time,json,paramiko,ConfigParser,os
from datetime  import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.forms.models import model_to_dict

# Create your views here.

def  index(request):
   
    return render(request, 'index.html', locals())


