from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from hangman.models import GameUser as User
from hangman.models import Game
import json

@staff_member_required
def home(request):

    return render(request, 'hangman/index.html', {})

@staff_member_required
@csrf_exempt #Disabling CSRF protection for simplicity's sake
def game_data(request):
    # Next time will use a custom user model instead of proxy model
    user = User.objects.get(pk=request.user.pk)
    game = user.current_game
    if request.method == "POST":
        if "newGame" in request.body:
            game = Game.objects.create(user=user)
        elif "guess" in request.body:
            guess = json.loads(request.body)["guess"]
            game.make_guess(guess)
    return HttpResponse(game.json, content_type="application/json")

