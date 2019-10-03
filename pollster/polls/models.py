from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')

    # Make question_text human readable
    def __str__(self):
        return self.question_text
    

# models.CASCADE is if the question is deleted, the choices gets deleted too.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Make choice_text human readable
    def __str__(self):
        return self.choice_text    