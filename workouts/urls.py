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
    path('workout/new/', views.workout_create, name='workout_create'),
    path('workout/<int:workout_pk>/add-set/', views.add_set_to_workout, name='add_set_to_workout'),
    path('workout/<int:pk>/edit/', views.WorkoutUpdateView.as_view(), name='workout_edit'),
    path('workout/<int:pk>/delete/', views.WorkoutDeleteView.as_view(), name='workout_delete'),
    path('templates/', views.template_list, name='template_list'),
    path('templates/<int:pk>/', views.template_detail, name='template_detail'),
    path('template/<int:pk>/start/', views.start_from_template, name='start_from_template'),


]
