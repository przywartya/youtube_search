from django.db import models
from django.conf import settings


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    video = models.CharField(max_length=256)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    RATING_CHOICES = (
        (0, 'Terrible'),
        (1, 'Boring'),
        (2, 'Okay'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Masterpiece'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
