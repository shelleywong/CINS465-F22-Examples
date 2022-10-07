from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class AnswerForm(forms.Form):
    answer_field = forms.CharField(
        label="Your Answer",
        max_length=280,
        validators=[
            validators.MinLengthValidator(3, message="Ensure Your Answer has at least 3 characters (it has 2)."),
            must_not_be_all_caps
        ])

    def save(self, request, quest_id):
        a_instance = models.AnswerModel()
        a_instance.answer_text = self.cleaned_data["answer_field"]
        a_instance.author = request.user
        q_instance = models.QuestionModel.objects.get(id=quest_id)
        a_instance.question = q_instance
        a_instance.save()
        return a_instance

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
