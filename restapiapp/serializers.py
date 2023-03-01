#./todo/serializers.py

from rest_framework import serializers
from restapiapp.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"