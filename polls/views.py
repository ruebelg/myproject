from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
from django.http import HttpResponse

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % (poll_id,))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("<strong></strong> You're voting on poll %s." % (poll_id,))
