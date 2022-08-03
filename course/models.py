from django.db import models

# Create your models here.
# Category -- Student_Course (M2M)


class Category (models.Model):
    cat_name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.cat_name


class Student_Course(models.Model):
    student = models.ForeignKey(
        Student, related_name='student_course', on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, related_name='student_course', on_delete=models.CASCADE)
