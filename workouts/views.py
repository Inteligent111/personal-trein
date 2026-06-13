from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Exercise  
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
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




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('workouts:exercise_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
    