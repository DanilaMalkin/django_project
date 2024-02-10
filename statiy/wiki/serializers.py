
from rest_framework import serializers
from .models import Articles
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']

class ArticlesSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Articles
        fields = "__all__"




