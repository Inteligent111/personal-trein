from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Exercise, Workout, WorkoutSet
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, WorkoutForm, WorkoutSetForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
    


@login_required
def my_workouts(request):
    workouts = request.user.workout.all() 
    context = {
        'workouts': workouts,
        }
    return render(request, 'workouts/my_workouts.html', context)




@login_required
def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user) 
    sets = WorkoutSet.objects.filter(workout=workout).select_related('exercise')
    context = {
        'workout': workout,
        'sets': sets,
    }
    return render(request, 'workouts/workouts_detail.html', context)




@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('workouts:my_workouts')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'workouts/edit_profile.html', {'form': form})




@login_required
def profile(request):
    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, 'workouts/profile.html', context)




@login_required
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workouts:my_workouts')
    else:
        form = WorkoutForm()
    return render(request, 'workouts/workout_form.html', {'form': form})




@login_required
def add_set_to_workout(request, workout_pk):  # Имена точно по ТЗ
    workout = get_object_or_404(Workout, id=workout_pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutSetForm(request.POST)
        if form.is_valid():
            workout_set = form.save(commit=False)
            workout_set.workout = workout
            workout_set.save()
            return redirect('workouts:workout_detail', pk=workout.id)
    else:
        form = WorkoutSetForm()
    return render(request, 'workouts/workout_set_form.html', {'form': form, 'workout': workout})




class WorkoutUpdateView(LoginRequiredMixin, UpdateView):
    
    model = Workout
    fields = ['name', 'date', 'notes']
    template_name = 'workouts/workout_form.html'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def success_url(self):
        return reverse_lazy('workouts:workouts_detail', kwargs={'pk': self.object.id})


class WorkoutDeleteView(LoginRequiredMixin, DeleteView):

    model = Workout
    template_name = 'workouts/workout_confirm_delete.html'
    success_url = reverse_lazy('workouts:my_workouts')

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)