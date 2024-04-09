from django.shortcuts import render

def home(request):
    """ Returns the index/home page """
    template = 'home/index.html'
    return render(request, template)
