from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),    # path('', hello)
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.project),
    path('tasks/', views.task),
]