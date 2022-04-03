# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import csv, os
import requests
from requests.exceptions import RequestException
import glob
import pandas as pd


# Database Models...
class User(models.Model):
    user_id = models.IntegerField()
    area = models.CharField(max_length=10)
    tariff = models.CharField(max_length=10)

class Consumption(models.Model):
    user_id = models.IntegerField(default=True)
    datetime = models.DateTimeField()
    consumption = models.FloatField()
 
