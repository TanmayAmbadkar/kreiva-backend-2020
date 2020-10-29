from django.db import models

# Create your models here.

class Event(models.Model):

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200, blank=True)
    long_description = models.TextField(blank=True)
    prize = models.IntegerField(blank=True)
    team_size = models.IntegerField(blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    rules_doc = models.FileField(upload_to='rules/', blank=True)

    def __str__(self):

        return self.name

class Member(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)

    def __str__(self):

        return f"{self.event}: {self.first_name} {self.role}"
