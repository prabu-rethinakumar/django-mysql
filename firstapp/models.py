# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Grade(models.Model):
    role = models.CharField(max_length=20)
    net_pay = models.IntegerField(default=75000)
    def __str__(self):
        return self.role


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    role = models.ForeignKey(Grade, on_delete=models.CASCADE)
    def __str__(self):
	return self.first_name

