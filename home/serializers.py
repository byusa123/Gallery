from rest_framework import serializers
from .models import *


        # fields = ['url', 'username', 'email', 'is_staff']
        
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        depth1=1
        fields=('__all__')
        


