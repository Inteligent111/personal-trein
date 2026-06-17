from django.urls import path
from . import views


app_name = 'workouts'


urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('my-workouts/', views.my_workouts, name='my_workouts'),
    path('workout/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
]
