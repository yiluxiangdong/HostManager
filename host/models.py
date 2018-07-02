<<<<<<< HEAD
=======
#coding:utf-8
>>>>>>> django项目2018/07/02 14:39:14 更新
from __future__ import unicode_literals

from django.db import models

# Create your models here.
<<<<<<< HEAD
=======

class Host(models.Model):
    ip = models.CharField(max_length=20,null=False)
    time = models.CharField(max_length=50, null=False)
    team = models.CharField(max_length=50, null=False)
    pctype = models.CharField(max_length=50)
    def __str__(self):
        return  self.ip


class User(models.Model):
    userID = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    idcard = models.EmailField(max_length=70)
    def __str__(self):
        return  self.name


class House(models.Model):
    houseid = models.CharField(max_length=20)
    mobile = models.CharField(max_length=50)
    landlord_id = models.CharField(max_length=50)
    org_id = models.EmailField(max_length=70)
    name = models.CharField(max_length=50)
    housestatus = models.CharField(max_length=50)

    def __str__(self):
        return  self.name
>>>>>>> django项目2018/07/02 14:39:14 更新
