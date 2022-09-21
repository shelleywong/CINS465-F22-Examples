from django.db import models
import datetime

# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(max_length=280)
   # pub_date = models.DateTimeField(default=datetime.date.today)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ID: " + str(self.id) + ", " + self.question_text + ", " + str(self.pub_date.strftime("%d %b %Y"))
