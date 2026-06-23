from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Exercise(models.Model):
    MUSCLE_GROUPS = [
        ('chest', 'Грудь'),
        ('back', 'Спина'),
        ('legs', 'Ноги'),
        ('shoulders', 'Плечи'),
        ('arms', 'Руки'),
        ('core', 'Кор'),
        ('cardio', 'Кардио'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    muscle_group = models.CharField(max_length=20, choices=MUSCLE_GROUPS)
    equipment = models.CharField(max_length=100, blank=True)
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    media_file = models.ImageField(upload_to='exercises/', blank=True, null=True)

    def __str__(self):
        return self.title




class UserProfile(models.Model):

    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]
    GOAL_CHOICES = [
        ('lose', 'Похудеть'),
        ('maintain', 'Удержать вес'),
        ('gain', 'Набрать массу'),
    ]



    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    birth_year = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    height_cm = models.PositiveIntegerField(blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, blank=True)
    daily_calories_target = models.PositiveIntegerField(blank=True, null=True)



    def __str__(self):
        return f"Профиль {self.user.username}"
    




class Workout(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='workout',
    )
    name = models.CharField(max_length=200, blank=True)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']


    def __str__(self):
        return f"{self.user.username}: {self.name or 'Тренировка'} ({self.date})"




class WorkoutSet(models.Model):

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='sets')
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    set_number = models.PositiveIntegerField()
    weight = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    reps = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['workout', 'set_number']

    def __str__(self):
        return f"{self.workout.user.username} : {self.exercise.title} X {self.set_number}"




class WorkoutTemplate(models.Model):

    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class WorkoutTemplateExercise(models.Model):
    template = models.ForeignKey(
        WorkoutTemplate,
        on_delete=models.CASCADE,
        related_name='template_exercises',
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    target_sets = models.PositiveIntegerField(default=3)
    target_reps = models.PositiveIntegerField(default=10)


    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.exercise.title} в шаблоне {self.template.name}"


