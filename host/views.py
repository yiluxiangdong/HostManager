#coding:utf-8
from django.http import JsonResponse
from django.shortcuts import render_to_response,redirect,HttpResponse,render,HttpResponseRedirect
from .models import *
<<<<<<< HEAD
=======
from django.http import JsonResponse
>>>>>>> django项目2018/07/02 14:39:14 更新
import time,json,paramiko,ConfigParser,os
from datetime  import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.forms.models import model_to_dict
<<<<<<< HEAD
=======
from t_rms_host import *
>>>>>>> django项目2018/07/02 14:39:14 更新

# Create your views here.

def  index(request):
<<<<<<< HEAD
   
    return render(request, 'index.html', locals())

=======
    return render(request, 'index.html', locals())

def selectuser(request):
    name = str(request.POST['name']).strip()
    try:
        data = User.objects.filter(name__contains=name).values('id','idcard','name','mobile')
        if data:
            return JsonResponse(json.dumps({'data': list(data),'status':1}), safe=False)
        else:
            return JsonResponse(json.dumps({'data': '','status':0}), safe=False)
    except Exception as e:
        print e


def delteuser(request,id):
    return HttpResponse('删除的用户id为：{}'.format(id))

def updateuser(request,id):
    return HttpResponse('更新的用户id为：{}'.format(id))



def selecthouse(request):
    name = request.POST['name']
    try:
        house = SelectDB()
        data = house.selectHouse(name)
        if data:
            return JsonResponse(json.dumps({'data': list(data),'status': 1}), safe=False)
        else:
            return JsonResponse(json.dumps({'data': '','status':0}), safe=False)
    except Exception as e:
        print e



def deltehouse(request,id):
    return HttpResponse('删除的房源id为：{}'.format(id))

def updatehouse(request,id):
    return HttpResponse('更新的房源id为：{}'.format(id))

>>>>>>> django项目2018/07/02 14:39:14 更新

