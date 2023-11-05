from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)  
    age = serializers.IntegerField()  
    class Meta:
        model=Student
        fields='__all__'
        
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error':'age cannot be less than 18'})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise  serializers.ValidationError({'error':'name cannot contian number'})

        return data
    