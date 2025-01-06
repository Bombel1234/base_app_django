from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

def index(request):
    # t = render_to_string('woman/index.html')
    # return HttpResponse(t)
    athlete_list = ['Facebook', 'Apply', 'Windows']
    data = {
        'title': 'Content site',
        'lst': athlete_list
    }
    return render(request, 'woman/index.html', data)
