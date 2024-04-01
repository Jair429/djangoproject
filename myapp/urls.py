from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('about/', views.about),
    path('hello/<str:jugador>', views.hello),
    path('projects/', views.projects),
    # path('tasks/<srt:title>', views.tasks),

]
