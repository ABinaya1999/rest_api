from rest_framework import serializers
from .models import *


class StudentSerializers(serializers.ModelSerializer):
    
    
    class Meta:
        models=Student
        fields='__all__'
    