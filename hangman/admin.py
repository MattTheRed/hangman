from django.contrib import admin
from hangman.models import GameUser as User
from hangman.models import Game

admin.site.register(User)
admin.site.register(Game)

# Register your models here.


