from django.db import models

class Question(models.Model):
    message = models.CharField(max_length=250)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.BooleanField()
