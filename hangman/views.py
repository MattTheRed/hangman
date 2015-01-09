from django.shortcuts import render

def home(request):
    return render(request, 'hangman/index.html', {})


# Create your views here.
