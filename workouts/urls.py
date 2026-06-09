from django.urls import path
from . import views


app_name = 'workouts'


urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
]
