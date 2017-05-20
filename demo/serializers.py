from rest_framework import serializers
from .models import Publisher
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields=['name','address','city','state_province','country','website',]