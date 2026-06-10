from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Exercise  
# Create your views here.

def exercise_list(request):
    selected_group = request.GET.get('group')

    exercises = Exercise.objects.all().order_by('muscle_group', 'title')

    if selected_group:
        exercises = exercises.filter(muscle_group=selected_group)

    context = {
        'exercises': exercises,
        'selected_group': selected_group,
        'muscle_groups': Exercise.MUSCLE_GROUPS,
    }
    return render(request, 'workouts/exercise_list.html', context)




def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)

    return render (request, 'workouts/exercise_detail.html', {'exercise': exercise})