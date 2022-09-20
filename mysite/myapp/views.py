from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request, page=0):
    #return HttpResponse("Hello, world! CINS 465!")
    page_list = list(range(page*10, page*10 + 10, 1))
    squares_list = [x**2 for x in range(10)]
    q_list = models.QuestionModel.objects.all()
    context = {
        'first_name': 'Shelley',
        'last_name': 'Wong',
        'title': 'CINS465',
        'msg': 'Hello World',
        'squares_list': squares_list,
        'page_list': page_list,
        'prev_page': page - 1,
        'next_page': page + 1,
        'q_list': q_list,
    }
    return render(request, "index.html", context=context)
