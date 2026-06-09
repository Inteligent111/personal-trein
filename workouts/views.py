from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise  
# Create your views here.

def exercise_list(request):
    exercises = Exercise.objects.all().order_by('muscle_group', 'title')
    return render(request, 'workouts/exercise_list.html', {'exercises': exercises})