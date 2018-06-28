from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the stringsomedays index.")
    
def detail(request, team_id):
    return HttpResponse("You're looking at team %s." % team_id)
