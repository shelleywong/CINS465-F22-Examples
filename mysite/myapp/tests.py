from django.test import TestCase
from django.contrib.auth import get_user_model
from django import forms as django_forms
from . import models
from . import forms

# Create your tests here.
class QuestionTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword'
        )
        user.save()
        user_instance = get_user_model().objects.get(id = 1)
        models.QuestionModel.objects.create(
            question_text = "cat?",
            author = user_instance
        )

    def test_question_to_str(self):
        """QuestionModel __str__ returns the expected string"""
        cat = models.QuestionModel.objects.get(question_text="cat?")
        self.assertEqual(str(cat), "john, cat?")

class NotAllCaps(TestCase):
    def setUp(self):
        pass

    def test_not_all_caps(self):
        """Test must_not_be_all_caps method catches NOT all caps"""
        self.assertEqual(forms.must_not_be_all_caps("not ALLCAPS!"), "not ALLCAPS!")

    def test_all_caps(self):
        """Tests must_not_be_all_caps method catches ALL CAPS"""
        self.assertRaises(
            django_forms.ValidationError,
            forms.must_not_be_all_caps,
            "ALLCAPS!"
        )
