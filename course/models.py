from django.db import models


# Category Model

class Category (models.Model):
    track = models.CharField(max_length=50)
    courses = models.ForeignKey(Course)

    def __str__(self):
        return self.track
