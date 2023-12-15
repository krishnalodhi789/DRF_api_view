"""
URL configuration for task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/student/<int:id>/", views.student_info),
    path("api/student_list/", views.student_list),
    path("api/stu_regi/", views.stu_regi),
    path("api/insert_stu_list/", views.insert_stu_list),
    path("api/create_user/", views.create_user),
    path("api/get_user/", views.get_user),
    path("api/delete_stu/<int:pk>/", views.delete_stu),
    path("api/update_stu/<int:pk>/", views.update_stu),
    # path("api_view/getStudentListOrInsertStudent/",views.GetStudentListOrInsertStudent.as_view()),
    path("api_view/getStudentListOrInsertStudent/",views.GetStudentListOrInsertStudent),
    path("api_view/get_one_user_OR_delete_update/<int:id>/",views.get_one_user_OR_delete_update),
    
    
]
