from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializer import StudentSerializer,UserSerializer
from .models import Student
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,ParseError
from django.views.decorators.csrf import csrf_exempt
import json
import io
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def student_info(request,id):
    stu = Student.objects.get(pk=id)
    serialize = StudentSerializer(stu)
    return JsonResponse(serialize.data)
    
    # data= JSONRenderer().render(serialize.data)
    # print(data)
    # return HttpResponse(data, content_type = 'application/json')
    
    
def student_list(request):
    stu_list = Student.objects.all()
    serializer = StudentSerializer(stu_list, many=True)
    # return JsonResponse(serializer.data,safe=False)

    data= JSONRenderer().render(serializer.data)
    print(data)
    return HttpResponse(data, content_type = 'application/json')
    
@csrf_exempt          
def stu_regi(req):
    if req.method == "POST":
        parsed_data = JSONParser().parse(req)
        serializer = StudentSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res = {'message': "Created.."}
            data= JSONRenderer().render(serializer.data)
            return HttpResponse(data, content_type='application/json')
            
        error= JSONRenderer().render(serializer.errors)
        print(" Errpr==============")
        print(error)
        return HttpResponse(error, content_type='application/json',)
            
            
@csrf_exempt
def insert_stu_list(request):
    if request.method == 'POST':
        parse_data = JSONParser().parse(request)
        serializer = StudentSerializer(data=parse_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        
        data = JSONParser().parse(serializer.errors)
        return JsonResponse(data, safe=False)
        
        
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        parseData = JSONParser().parse(request)
        serializer  = UserSerializer(data=parseData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
    
    
def get_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
    
    
        
@csrf_exempt    
def delete_stu(request, pk):
    if request.method=="DELETE":
        try:
            stu = Student.objects.get(pk=pk)
            stu.delete()
            return HttpResponse(status=200)
        except :
           return HttpResponse(status=404)
       
    
        
@csrf_exempt 
def update_stu(req,pk):
    if req.method == "PUT":
        try:
            stu=Student.objects.get(pk=pk)
            paserData = JSONParser().parse(req)
            serializer = StudentSerializer(stu, data=paserData)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse(serializer.errors, safe=False)
        except :
            return HttpResponse(status=404)
        
       
    
@api_view(['GET','POST'])
def GetStudentListOrInsertStudent(request):
    if request.method == "GET":
        try:
            users = User.objects.all()
            serializers = UserSerializer(users, many=True)
            context = {
                "success": True,
                "status":status.HTTP_200_OK,
                "data":serializers.data
                
            }
            return Response(context)
        
        except Exception as e:
            context = {
                    "success": False,
                    "status":status.HTTP_400_BAD_REQUEST,
                    "data": e
                    
                }
            return Response(context)

    if request.method == "POST":
       try:
            serializers = UserSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                context={
                    "sucess":True,
                    "status":status.HTTP_201_CREATED,
                    "data":serializers.data
                }
                return Response(context)
       except Exception as e:
            print("dfksh")
            context={
                "sucess":False,
                "status":status.HTTP_400_BAD_REQUEST,
                "data":e
            }
            return Response(context)
            

# from rest_framework.views import APIView    
# class GetStudentListOrInsertStudent(APIView):
#     def get(request,*args, **kwargs):
#         try:
            
        
#             users = User.objects.all()
#             serializers = UserSerializer(users, many=True)
#             return Response(serializers.data)

#         except Exception as E:
#             return Response(str(E))
            
@api_view(["GET","DELETE","PUT"])
def get_one_user_OR_delete_update(request,id):
    if request.method=="GET":
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            context={
                "success":True,
                "status":status.HTTP_200_OK,
                "data":serializer.data
            }
            return Response(context)
        except Exception as e:
            context={
                "success":False,
                "status":status.HTTP_400_BAD_REQUEST,
                "data":serializer.data
            }  
            return Response(context)
        
    if request.method=="PUT":
        try:
            user = User.objects.get(id=id)
            print(user.username)
            print(request.data)
            serializer = UserSerializer(user, data=request.data, partially = True)
            if serializer.is_valid():
                serializer.save()
                context={
                    "success":True,
                    "status":status.HTTP_205_RESET_CONTENT,
                    "data":serializer.data
                }
                return Response(context)
        except Exception as e:
            context={
                "success":False,
                "status":status.HTTP_400_BAD_REQUEST,
                "data":serializer.data
            }  
            return Response(context)