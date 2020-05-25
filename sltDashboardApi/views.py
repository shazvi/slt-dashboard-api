from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from sltDashboardApi.models import Hero, HourlyUsage
from sltDashboardApi.serializers import UserSerializer, GroupSerializer, HeroSerializer, HourlyUsageSerializer


class UserViewSet(viewsets.ModelViewSet):
	# Api endpoints that allow a user to be viewed or edited
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	# Api endpoints that allow a group to be viewed or edited
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]


class HeroViewSet(viewsets.ModelViewSet):
	# Api endpoints that allow a hero to be viewed or edited
	queryset = Hero.objects.all().order_by('name')
	serializer_class = HeroSerializer


class HourlyUsageViewSet(viewsets.ModelViewSet):
	# Api endpoints that allow an hourly Usage to be viewed or edited
	queryset = HourlyUsage.objects.all().order_by('date_time')
	serializer_class = HourlyUsageSerializer
