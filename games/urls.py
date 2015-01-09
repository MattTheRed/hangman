from django.conf.urls import patterns, include, url
from django.contrib import admin
from hangman.models import GameUser as User
from hangman.models import Game

urlpatterns = patterns('',
    url(r'^$', 'hangman.views.home', name='home'),
    url(r'^game-data/', 'hangman.views.game_data', name='game_data'),
    url(r'^admin/', include(admin.site.urls)),
)


