from django.db import models

class user(models.Model):
	usr = models.CharField(max_length=200)

class email(models.Model):
	usr_email = models.CharField(max_length=200)

class password(models.Model):
	usr_pwd = models.CharField(max_length=200)

class first_name(models.Model):
	usr_first = models.CharField(max_length=200)

class last_name(models.Model):
	usr_last = models.CharField(max_length=200)

# Create your models here.
