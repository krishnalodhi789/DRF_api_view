from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User



class StudentSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=30)
    city= serializers.CharField(max_length=30)
    age= serializers.IntegerField()
    id=serializers.IntegerField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, student, validated_data):
        updated_Student=Student(**validated_data)
        updated_Student.id=student.id
        updated_Student.save()
        
        # print(student.name)
        # updated_Student = Student.objects.get(id=student.id)
        # updated_Student.name= validated_data.get("name",student.name)
        # print(student.name)
        # updated_Student.city= validated_data.get("city",student.city)
        # updated_Student.age= validated_data.get("age",student.age)
        # updated_Student.save()
        
        return updated_Student
    
    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=32,)
    
    def create(self, validates_data):
        return User.objects.create(**validates_data)
    
    def update(self, instance, validated_data):
        updated_user = User(**validated_data)
        updated_user.id = instance.id
        return updated_user.save()
    
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
            