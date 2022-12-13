from django.db import models

class Event(models.Model):
	name = models.CharField('Name', max_length=60)
	major = models.CharField('Major', max_length=60)
	graduate = models.CharField('Graduation Date', max_length=4)
	current = models.CharField('Current Employment', max_length=360)
	img = models.ImageField()


	def __str__(self):
		return self.name


class User(models.Model):
	username = models.CharField('Username', max_length=24)
	email = models.EmailField('Email', max_length=60)

	def __str__(self):
		return self.username
