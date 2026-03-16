from rest_framework import serializers
from .models import Dream

class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ['id', 'title', 'description', 'tags', 'created_at']
        read_only_fields = ['created_at']