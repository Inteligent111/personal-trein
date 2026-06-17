from django.forms import ModelForm
from .models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_year', 'gender', 'height_cm', 'weight_kg', 'goal']
