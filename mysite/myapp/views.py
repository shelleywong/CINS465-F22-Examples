from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, page=0):
    #return HttpResponse("Hello, world! CINS 465!")
    page_list = list(range(page*10, page*10 + 10, 1))
    squares_list = [x**2 for x in range(10)]
    context = {
        'first_name': 'Shelley',
        'last_name': 'Wong',
        'title': 'CINS465',
        'msg': 'Hello World',
        'squares_list': squares_list,
        'page_list': page_list,
        'prev_page': page - 1,
        'next_page': page + 1,
    }
    return render(request, "index.html", context=context)
