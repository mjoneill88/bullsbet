from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model)
    text = models.Charfield(max_length=400)
    correct = models.CharField(max_length=1) #one letter for A or B which was "correct" or winning answer
    created_on = models.DateTimeField()


class Answer(models.Model)
    owner = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    pick = models.CharField(max_length=1) #one letter for A or B, team 1 or team 2, win or loss, take the bet or don't, etc
    win = models.BooleanField()

class User(models.Model)
