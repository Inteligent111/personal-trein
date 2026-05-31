from django.db import models

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

    def __str__(self):
        return self.title