from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [

    path('', TaskList.as_view(), name="TaskList"),
    path('TaskDetail/<int:pk>/', TaskDetail.as_view(), name="TaskDetail"),
    path('TaskCreate/', TaskCreate.as_view(), name="CreateTask"),
    path('TaskUpdate/<int:pk>/', TaskUpdate.as_view(), name="UpdateTask"),
    path('TaskDelete/<int:pk>/', TaskDelete.as_view(), name="DeleteTask"),


]