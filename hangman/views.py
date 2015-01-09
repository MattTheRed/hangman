from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from hangman.models import GameUser as User
from hangman.models import Game


@staff_member_required
def home(request):

    return render(request, 'hangman/index.html', {})

@staff_member_required
def game_data(request):
    # Next time will use a custom user model instead of proxy model
    user = User.objects.get(pk=request.user.pk)
    game = user.current_game
    if request.method == "POST":
        if "guess" in request.POST:
            if request.POST.get(""):
                pass
        pass
    else:
        return HttpResponse(game.json, content_type="application/json")

