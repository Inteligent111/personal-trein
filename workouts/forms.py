from django import forms
from django.forms import ModelForm
from .models import UserProfile, Workout, WorkoutSet


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_year', 'gender', 'height_cm', 'weight_kg', 'goal']



class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'date', 'notes']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Например: Грудь и трицепс (можно оставить пустым)'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date' # Это вызовет удобный календарик в браузере
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Заметки к тренировке...'
            }),
        }



class WorkoutSetForm(ModelForm):
    class Meta:
        model = WorkoutSet
        fields = ['exercise', 'set_number','weight' ,'reps', 'rest_seconds']  

          