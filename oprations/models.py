from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name