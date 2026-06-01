from django.contrib import admin
from .models import Exercise, UserProfile, Workout, WorkoutSet
# Register your models here.
admin.site.register(Exercise)
admin.site.register(UserProfile)
admin.site.register(Workout)
admin.site.register(WorkoutSet)