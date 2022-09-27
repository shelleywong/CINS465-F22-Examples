from django import forms
from django.core import validators
from . import models

def must_not_be_all_caps(value):
    if value.isupper():
        raise forms.ValidationError("Must not be in all caps. No need to shout!")
    # in all cases, return cleaned data
    return value

class QuestionForm(forms.Form):
    question_field = forms.CharField(
        label="Your Question",
        max_length=280,
        validators=[
            validators.MinLengthValidator(3, message="Ensure Your Question has at least 3 characters (it has 2)."),
            must_not_be_all_caps
        ])

    def save(self, request):
        q_instance = models.QuestionModel()
        q_instance.question_text = self.cleaned_data["question_field"]
        q_instance.author = request.user
        q_instance.save()
        return q_instance
