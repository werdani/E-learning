from django.db import models
from django.contrib.auth.models import User
from course.models import Course
# -----
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

class Review(models.Model):
    description = models.CharField(max_length=1000, null=True)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    
    def __str__(self):
        return f"{self.description}"
    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
