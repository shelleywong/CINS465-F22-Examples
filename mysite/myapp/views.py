from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import models
from . import forms

# Create your views here.
@login_required
def index(request, page=0):
    #return HttpResponse("Hello, world! CINS 465!")
    current_user = request.user
    page_list = list(range(page*10, page*10 + 10, 1))
    squares_list = [x**2 for x in range(10)]
    context = {
        'current_user': current_user,
        'title': 'CINS465',
        'msg': 'Hello World',
        'squares_list': squares_list,
        'page_list': page_list,
        'prev_page': page - 1,
        'next_page': page + 1,
    }
    return render(request, "index.html", context=context)

def questions(request):
    if request.method == "POST":
        q_form = forms.QuestionForm(request.POST)
        if q_form.is_valid() and request.user.is_authenticated:
            q_form.save(request)
            #q_form = forms.QuestionForm()
            return redirect("/questions/")

    else: # GET and all other HTTP methods
        q_form = forms.QuestionForm()

    q_objects = models.QuestionModel.objects.all()
    q_list = []
    for q in q_objects:
        temp_q = {}
        temp_q["question_text"] = q.question_text
        temp_q["pub_date"] = q.pub_date
        temp_q["author"] = q.author.username
        a_objects = models.AnswerModel.objects.filter(question=q)
        temp_q["answers"] = a_objects
        q_list += [temp_q]

    context = {
        'title': 'CINS 465 Questions',
        'q_form': q_form,
        'q_list': q_list,
    }
    return render(request, "questions.html", context=context)

def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("/login/")
    else:
        form = forms.RegistrationForm(request.POST)

    context = {
        "form": form
    }
    return render(request, "registration/register.html", context=context)

def logout_user(request):
    logout(request)
    return redirect("/login/")
