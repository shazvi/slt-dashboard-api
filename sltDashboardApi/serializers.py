from django.contrib.auth.models import User, Group
from rest_framework import serializers

from sltDashboardApi.models import Hero, HourlyUsage


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']


class HeroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Hero
		fields = ['url', 'name', 'alias']


class HourlyUsageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = HourlyUsage
		fields = ['date_time', 'total_limit', 'total_used', 'day_limit', 'day_used']
