from django import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AddInfo(models.Model):
    mapID = models.TextField(unique=False,null=False)
    location = models.CharField(max_length=100, null=True)
    profile_of_needs = models.CharField(max_length=100, null=True)
    registered_providers = models.TextField(unique=False,null=True)
    care_providers = models.TextField(unique=False,null=True)
    icb_contacts = models.TextField(unique=False,null=True)
    void_agreement = models.TextField(unique=False,null=True)
    additional_notes = models.TextField(unique=False,null=True)
    color = models.TextField(unique=False,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)


