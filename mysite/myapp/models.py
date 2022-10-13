# import datetime
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(max_length=280)
   # pub_date = models.DateTimeField(default=datetime.date.today)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(
        max_length = 144,
        upload_to = 'uploads/%Y/%m/%d/',
        null = True
    )
    image_description = models.CharField(max_length=280, null=True)

    def __str__(self):
        return self.author.username + ", " + self.question_text

class AnswerModel(models.Model):
    answer_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
