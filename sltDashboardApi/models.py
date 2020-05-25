from django.contrib.auth.models import User
from django.db import models


class Hero (models.Model):
	name = models.CharField(max_length=60)
	alias = models.CharField(max_length=60)

	def __str__(self):
		return self.name


class HourlyUsage (models.Model):
	date_time = models.DateTimeField(auto_now_add=True)
	total_limit = models.IntegerField()
	total_used = models.IntegerField()
	day_limit = models.IntegerField()
	day_used = models.IntegerField()


class UsageGroup (models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	usage = models.ForeignKey(HourlyUsage, on_delete=models.CASCADE)
