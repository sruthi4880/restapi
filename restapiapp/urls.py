#./todo/views.py

from django.urls import path
from . views import *

urlpatterns = [
    path('',ListTodoAPIView.as_view(),name='todo'),
    path('detail/<str:pk>/',TodoDetailAPIView.as_view(),name='detail'),
    path('create',CreateTodoAPIView.as_view(),name='create'),
    path('update/<str:pk>/',UpdateTodoAPIView.as_view(),name='update'),
    path('delete/<str:pk>/',DeleteTodoAPIView.as_view(),name='delete'),
]