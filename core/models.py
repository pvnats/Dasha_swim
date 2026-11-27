from django.db import models
from django.utils import timezone

class Swimmer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthday = models.DateField(auto_now=False)
    created = models.DateTimeField(default=timezone.now)
    sex = models.CharField(choices=(( 'F', 'Famale'), ('M', 'Male')))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    style = models.CharField()
    distance = models.IntegerField(default=25)
    repeat = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.style} {self.distance} м x {self.repeat}'


class Training(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    students = models.ManyToManyField(Swimmer)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.date_time} {len(self.students.values())}'


