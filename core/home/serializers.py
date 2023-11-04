from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)  
    age = serializers.IntegerField()  
    class Meta:
        model=Student
        fields='__all__'
    