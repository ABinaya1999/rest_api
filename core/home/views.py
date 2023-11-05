from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def home(request):
    record = Student.objects.all()
    serializer = StudentSerializers(record,many=True)
    return Response({'status':200,'students':serializer.data})


@api_view(['POST'])
def create(request):
 
    data = request.data
    serializer = StudentSerializers(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403,'error':serializer.errors,'message':'smth wrong'})
    serializer.save()
    return Response({'status':200,'students':serializer.data,'message':'data saved'})

# @api_view(['PUT'])
# def update_student(request,id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         data = request.data
#         serializer = StudentSerializers(student_obj,data = request.data,partial=True)
#         if not serializer.is_valid():
#             return Response({'status':403,'error':serializer.errors,'message':'smth wrong'})
#         serializer.save()
#         return Response({'status':200,'students':serializer.data,'message':'data saved'})
#     except Exception as e:
#         return Response({'status:403',{'msg':'invalid id'}})
    
    
# @api_view(['DELETE'])   
# def delete_student(request,id):
#     try:
#          student_obj = Student.objects.get(id=id)
#          student_obj.delete()
#          return Response({'status:403',{'msg':'data {id} deleted'}})
#     except Exception as e:
#         return Response({'status:403',{'msg':'invalid id'}})
        
    
    
        
    

   
    
    