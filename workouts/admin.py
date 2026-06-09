from django.contrib import admin
from .models import Exercise, UserProfile, Workout, WorkoutSet




class WorkoutSetInline(admin.TabularInline):
    model = WorkoutSet
    extra = 1




@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display =  ('title', 'muscle_group', 'equipment', 'created_at')
    list_filter = ('muscle_group',)
    search_fields = ('title', 'description')




@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'height_cm','weight_kg')
    list_filter = ('gender', 'goal')
    search_fields = ('user__username',)




@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('name', 'notes')
    inlines = [WorkoutSetInline]




@admin.register(WorkoutSet)
class WorkoutSetAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'set_number', 'weight', 'reps')
    list_filter = ('exercise',)
    


