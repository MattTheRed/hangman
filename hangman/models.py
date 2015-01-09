from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import string
import json

class GameUser(User):
    class Meta:
        proxy = True

    @property
    def wins(self):
        return Game.objects.filter(user=self, outcome="WIN").count()

    @property
    def losses(self):
        return Game.objects.filter(user=self, outcome="LOSS").count()

    def get_or_create_latest_game(self):
        try:
            return Game.objects.filter(user=self).order_by("-pk")[0]
        except:
            return Game.objects.create(user=self)

    @property
    def current_game(self):
        return self.get_or_create_latest_game()



class Word(models.Model):
    word = models.CharField(max_length=255)

    def __unicode__(self):
        return self.word

class Game(models.Model):
    user = models.ForeignKey(GameUser)
    word = models.ForeignKey(Word)
    # guess_count = models.PositiveSmallIntegerField(default=0)
    OUTCOME_CHOICES = (
        ('WIN', 'Win'),
        ('LOSS', 'Loss')
    )
    outcome = models.CharField(max_length=4, choices=OUTCOME_CHOICES)

    alphabet = list(string.ascii_uppercase)

    @property
    def guess_count(self):
        return Guess.objects.filter(game=self).count()

    @property
    def remaining_letters(self):
        letter_list = self.alphabet[:]
        for letter in self.guesses:
            letter_list.remove(letter.letter)
        return letter_list

    @property
    def json(self):
        data = {}
        data["score"] = {
            "wins": self.user.wins,
            "losses": self.user.losses,
            "game": {
                "guess_count": self.guess_count,
                "outcome": self.outcome,
                "remaining_letters": self.remaining_letters,
                "guesses": [guess.letter for guess in self.guesses]
            }
        }
        return json.dumps(data)

    @property
    def guesses(self):
        return Guess.objects.filter(game=self)

    def make_guess(self, letter):
        Guess.objects.create(game=self, letter=letter)

    def __unicode__(self):
        return self.word.word

    def save(self, *args, **kwargs):
        self.word = Word.objects.all().order_by("?")[0]
        super(Game, self).save(*args, **kwargs)

class Guess(models.Model):
    game = models.ForeignKey(Game)
    letter = models.CharField(max_length=1)
