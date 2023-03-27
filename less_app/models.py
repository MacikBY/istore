from django.db import models


# Create your models here.
class LessUser(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField('LessUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    hour = models.PositiveIntegerField()
    schools = models.ManyToManyField('School')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name
