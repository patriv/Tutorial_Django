from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','first_name','last_name')
